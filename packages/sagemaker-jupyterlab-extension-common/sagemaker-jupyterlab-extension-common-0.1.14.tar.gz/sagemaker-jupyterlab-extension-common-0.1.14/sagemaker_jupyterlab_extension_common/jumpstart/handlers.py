import datetime
import os
import uuid
from jupyter_events import EventLogger

from pydantic import ValidationError
from sagemaker_jupyterlab_extension_common.util.app_metadata import get_region_name
from sagemaker_jupyterlab_extension_common.jumpstart.stage_utils import (
    is_jumpstart_supported_region,
)
from sagemaker_jupyterlab_extension_common.handlers import JupterLabUILogHandler
from sagemaker_jupyterlab_extension_common.logging.logging_utils import (
    SchemaDocument,
    create_ui_eventlogger,
)
from sagemaker_jupyterlab_extension_common.jumpstart.logging_utils import (
    JumpStartHandlerLogMixin,
)
from sagemaker_jupyterlab_extension_common.exceptions import (
    NotebookTooLargeError,
    S3ObjectNotFoundError,
)
from sagemaker_jupyterlab_extension_common.executor import (
    ProcessExecutorUtility,
)
from sagemaker_jupyterlab_extension_common.jumpstart.constants import (
    CLIENT_REQUEST_ID_HEADER,
    HOME_PATH,
    MISSING_CLIENT_REQUEST_ID,
    NOTEBOOK_PATH,
    NOTEBOOK_SIZE_LIMIT_IN_MB,
    ErrorCode,
)
from sagemaker_jupyterlab_extension_common.jumpstart.notebook_utils import (
    _get_notebook_content,
    get_jumpstart_notebook_name,
    notebook_transformation_needed,
)
from sagemaker_jupyterlab_extension_common.jumpstart.request import (
    NotebookRequest,
    client_request_id_var,
    server_request_id_var,
)
from sagemaker_jupyterlab_extension_common.file_utils import save_to_ebs
from sagemaker_jupyterlab_extension_common.jumpstart.notebook_transformation import (
    InferNotebook,
    ModelSdkNotebook,
)
from sagemaker_jupyterlab_extension_common.jumpstart.notebook_types import (
    JumpStartResourceType,
)
import traceback
import json
from jupyter_server.base.handlers import JupyterHandler
from jupyter_server.utils import url_path_join
from tornado import web

ProcessExecutorUtility.initialize_executor(max_workers=4)


def transform_notebook(
    request: NotebookRequest,
    content: str,
):
    resource_type = request.resource_type
    model_id = request.js_model_id
    endpoint_name = request.endpoint_name
    inference_component = request.inference_component
    key = request.key

    if notebook_transformation_needed(resource_type):
        if resource_type == JumpStartResourceType.inferNotebook:
            content = InferNotebook().transform(
                content, endpoint_name, inference_component
            )
        elif resource_type == JumpStartResourceType.modelSdkNotebook:
            content = ModelSdkNotebook().transform(content, model_id)

    # save notebook to home dir
    file_path = save_to_ebs(
        NOTEBOOK_PATH,
        get_jumpstart_notebook_name(model_id, key, resource_type),
        content,
    )
    # docmanager:open expect a relative path, trim HOME_PATH and return a relative path.
    # if the file_path is not under HOME_PATH, return the full path.
    if file_path.startswith(HOME_PATH):
        notebook_path = os.path.relpath(file_path, HOME_PATH)
    else:
        notebook_path = file_path

    return notebook_path


class JumpStartNotebookHandler(JumpStartHandlerLogMixin, JupyterHandler):
    """A Handler to download notebook from s3 to memory and substitue notebook based on resource_type and save to file"""

    def set_header_context(self):
        # set client_request_id context var
        client_request_id = self.request.headers.get(
            CLIENT_REQUEST_ID_HEADER, MISSING_CLIENT_REQUEST_ID
        )
        client_request_id_var.set(client_request_id)
        # set server_request_id context var
        server_request_id = str(uuid.uuid4())
        server_request_id_var.set(server_request_id)
        # set header
        self.set_header("Content-Type", "application/json")
        self.set_header("X-Server-Req-Id", server_request_id)

    @web.authenticated
    async def post(self):
        """Download notebook from s3 to memory and substitue notebook based on resource_type and save to file"""
        start_time = datetime.datetime.now()
        self.set_header_context()
        self.log.info(f"Calling JumpStart notebook handler")
        if not is_jumpstart_supported_region():
            self.log.error(
                f"Invalid region to download JumpStart notebook. Region: [{get_region_name()}]"
            )
            self.set_status(404)
            self.finish(
                json.dumps(
                    {
                        "errorCode": ErrorCode.NOTEBOOK_NOT_AVAILABLE,
                        "errorMessage": "The JumpStart notebook is not available in the current region",
                    }
                )
            )
            return
        try:
            body = self.get_json_body()
            model = NotebookRequest(**body)
            content = await _get_notebook_content(model.key)
            notebook_path = await ProcessExecutorUtility.run_on_executor(
                transform_notebook, model, content
            )
            elapsedTime = datetime.datetime.now() - start_time
            self._emit_latency_metric(elapsedTime)
            self.log.info(
                f"Successfully downloaded JumpStart notebook to {notebook_path}. model_id: [{model.js_model_id}], s3_key:[{model.key}]"
            )
            self.set_status(200)
            self.finish(json.dumps({"notebookPath": notebook_path}))
        except ValidationError as error:
            self.log.error(f"Invalid request: {traceback.format_exc()}")
            self._emit_latency_metric(datetime.datetime.now() - start_time)
            self._emit_error_metric()
            self.set_status(400)
            self.finish(
                json.dumps(
                    {
                        "errorCode": ErrorCode.INVALID_REQUEST,
                        "errorMessage": "Invalid request or wrong input.",
                    }
                )
            )
        except S3ObjectNotFoundError as error:
            self.log.error(
                f"Notebook not found: {traceback.format_exc()}. model_id: [{model.js_model_id}], s3_key:[{model.key}]"
            )
            self._emit_latency_metric(datetime.datetime.now() - start_time)
            self._emit_error_metric()
            self.set_status(404)
            self.finish(
                json.dumps(
                    {
                        "errorCode": ErrorCode.NOTEBOOK_NOT_AVAILABLE,
                        "errorMessage": "Notebook not found",
                    }
                )
            )
        except NotebookTooLargeError as error:
            self.log.error(
                f"Notebook too large: {traceback.format_exc()}. model_id: [{model.js_model_id}], s3_key:[{model.key}]"
            )
            self._emit_latency_metric(datetime.datetime.now() - start_time)
            self._emit_error_metric()
            self.set_status(413)
            self.finish(
                json.dumps(
                    {
                        "errorCode": ErrorCode.NOTEBOOK_SIZE_TOO_LARGE,
                        "errorMessage": f"Notebook size exceeds {NOTEBOOK_SIZE_LIMIT_IN_MB}MB",
                    }
                )
            )
        except Exception as error:
            self.log.error(
                f"Failed to get jumpstart notebook: {traceback.format_exc()}. model_id: [{model.js_model_id}], s3_key:[{model.key}]"
            )
            self._emit_latency_metric(datetime.datetime.now() - start_time)
            self._emit_fault_metric()
            self.set_status(500)
            self.finish(
                json.dumps(
                    {
                        "errorCode": ErrorCode.INTERNAL_SERVER_ERROR,
                        "errorMessage": str(error),
                    }
                )
            )


class JumpStartJupterLabUILogHandler(JupterLabUILogHandler):
    """Handle event log requests emitted by JumpStart's extension"""

    eventlog_instance = None

    def get_eventlogger(self) -> EventLogger:
        if not JumpStartJupterLabUILogHandler.eventlog_instance:
            """ "Create a StudioEventLog with the correct schemas"""
            schema_documents = [
                SchemaDocument.JumpStartJupyterLabOperation,
            ]
            JumpStartJupterLabUILogHandler.eventlog_instance = create_ui_eventlogger(
                schema_documents
            )
        return JumpStartJupterLabUILogHandler.eventlog_instance


def build_url(web_app, endpoint):
    base_url = web_app.settings["base_url"]
    return url_path_join(base_url, endpoint)


def register_jumpstart_handlers(nbapp):
    web_app = nbapp.web_app
    host_pattern = ".*$"
    handlers = [
        (
            build_url(web_app, r"/aws/sagemaker/api/jumpstart/notebook"),
            JumpStartNotebookHandler,
        ),
        (
            build_url(web_app, r"/aws/sagemaker/api/jumpstart/eventlog"),
            JumpStartJupterLabUILogHandler,
        ),
    ]
    web_app.add_handlers(host_pattern, handlers)
