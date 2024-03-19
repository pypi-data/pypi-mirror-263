"""This notebook util is translated based on 
https://code.amazon.com/packages/RhinestoneSagemakerUI/blobs/mainline/--/packages/sagemaker-ui-graphql-server/src/services/penny/utils/notebookUtils.ts
https://code.amazon.com/packages/SageMakerHubJavascriptSDK/blobs/mainline/--/src/utils/notebookUtils.ts

TODO: refactor the update notebook logic to make it more clear and efficient
"""

import json
from typing import Optional
from sagemaker_jupyterlab_extension_common.jumpstart.constants import (
    JUMPSTART_ALTERATIONS,
    REMOVAL_OPERATIONS,
)
from sagemaker_jupyterlab_extension_common.jumpstart.notebook_types import (
    JumpStartModelNotebookAlterationType,
    JumpStartModelNotebookGlobalActionType,
    JumpStartModelNotebookSubstitution,
    JumpStartModelNotebookSubstitutionTarget,
    UpdateHubNotebookUpdateOptions,
)
from abc import ABC, abstractmethod
import nbformat


def _is_cell_replacement(alteration: JumpStartModelNotebookAlterationType) -> bool:
    if (
        alteration == JumpStartModelNotebookAlterationType.modelIdVersion
        or alteration == JumpStartModelNotebookAlterationType.modelIdOnly
    ):
        return True
    return False


def _is_cell_removal(alteration: JumpStartModelNotebookAlterationType) -> bool:
    if (
        alteration == JumpStartModelNotebookAlterationType.dropModelSelection
        or alteration == JumpStartModelNotebookAlterationType.dropForDeploy
        or alteration == JumpStartModelNotebookAlterationType.dropForTraining
    ):
        return True
    return False


def _should_remove_cell(notebook_cell: dict) -> bool:
    cell_alterations = notebook_cell["metadata"].get(JUMPSTART_ALTERATIONS)
    if not cell_alterations:
        return False
    try:
        return any(
            JumpStartModelNotebookAlterationType(alteration) in REMOVAL_OPERATIONS
            for alteration in cell_alterations
        )
    except ValueError:
        return False


def _get_substitue_cell(model_id: str, current_cell: dict) -> dict:
    current_alterations = current_cell.get("metadata", {}).get(
        JUMPSTART_ALTERATIONS, []
    )
    if not current_alterations:
        return current_cell
    # currently for each cell we only support one alteration
    current_alteration = current_alterations[0]
    if current_alteration == JumpStartModelNotebookAlterationType.modelIdVersion.value:
        current_cell["source"] = [f'model_id, model_version = "{model_id}", "*"']
    elif current_alteration == JumpStartModelNotebookAlterationType.modelIdOnly.value:
        current_cell["source"] = [f'model_id = "{model_id}"']
    return current_cell


def update_notebook(
    content: str, modelId: Optional[str], options: UpdateHubNotebookUpdateOptions
) -> str:
    """notebook transformation logic. it contains 3 options types to transform the notebook.
    1. remove cells required to be dropped.
    2. replace cells required to be replaced.
    3. substitute part of the cells based on endpoint_name and/or inference_component_name

    :param content: notebook content
    :param modelId: model id
    :param options: update notebook options
    :return: transformed notebook content.
    :raises ValueError: if notebook is not a valid JSON or if notebook validation fails.
    """
    try:
        nb = json.loads(content)
    except json.decoder.JSONDecodeError as je:
        raise ValueError(f"Notebook is not a valid JSON: {je}")

    # validate notebook by using nbformat version 4 schema
    # https://github.com/jupyter/nbformat/blob/main/nbformat/v4/nbformat.v4.schema.json
    try:
        nbformat.validate(nb, version=4)
    except nbformat.reader.ValidationError as ve:
        raise ValueError(f"Notebook validation failed: {ve}")

    completedSubstitutions = set()
    remove_alterations = [
        alteration for alteration in options.alterations if _is_cell_removal(alteration)
    ]
    replace_alterations = [
        alteration
        for alteration in options.alterations
        if _is_cell_replacement(alteration)
    ]

    # first: remove cells required to be dropped.
    if remove_alterations:
        nb["cells"] = [cell for cell in nb["cells"] if not _should_remove_cell(cell)]

    if JumpStartModelNotebookGlobalActionType.dropAllMarkdown in options.globalActions:
        nb["cells"] = [cell for cell in nb["cells"] if cell["cell_type"] != "markdown"]

    # second: perform alteration, ie remove or replace whole code cell.
    if replace_alterations and modelId:
        nb["cells"] = [
            _get_substitue_cell(modelId, cell) if cell["cell_type"] == "code" else cell
            for cell in nb["cells"]
        ]

    #  third: perform the substitutions, ie find/replace inside a code cells.
    if options.substitutions:
        for substitution in options.substitutions:
            for cell in nb["cells"]:
                if cell["cell_type"] == "code":
                    for i, line in enumerate(cell["source"]):
                        if substitution.find.value in line:
                            line = line.replace(
                                substitution.find.value, substitution.replace
                            )
                            cell["source"][i] = line
                            if substitution.onlyOnce:
                                completedSubstitutions.add(substitution.find)
                                break
                if substitution.find in completedSubstitutions:
                    break

    # fourth: clean notebook by clearing any output
    for cell in nb["cells"]:
        cell["outputs"] = []

    return json.dumps(nb)


class Notebook(ABC):
    @abstractmethod
    def transform(self, notebook: str, *args, **kwargs) -> str:
        """
        Transform the notebook.
        Args:
            notebook (str): The notebook to transform.
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.
        Returns:
            str: The transformed notebook.
        """
        pass


class InferNotebook(Notebook):
    def transform(
        self, notebook: str, endpointName: str, inferenceComponentName: Optional[str]
    ) -> str:
        substitutions = [
            JumpStartModelNotebookSubstitution(
                JumpStartModelNotebookSubstitutionTarget.endpointName,
                endpointName,
                True,
            )
        ]
        if inferenceComponentName:
            substitutions.append(
                JumpStartModelNotebookSubstitution(
                    JumpStartModelNotebookSubstitutionTarget.inferenceComponentTarget,
                    f"{JumpStartModelNotebookSubstitutionTarget.inferenceComponentTarget.value}, InferenceComponentName='{inferenceComponentName}'",
                    True,
                )
            )
        options = UpdateHubNotebookUpdateOptions(substitutions, [], [])
        notebook = update_notebook(notebook, None, options)
        return notebook


class ModelSdkNotebook(Notebook):
    def transform(self, notebook: str, modelId: str) -> str:
        alterations = [
            JumpStartModelNotebookAlterationType.dropModelSelection,
            JumpStartModelNotebookAlterationType.modelIdOnly,
            JumpStartModelNotebookAlterationType.modelIdVersion,
        ]
        options = UpdateHubNotebookUpdateOptions([], alterations, [])
        notebook = update_notebook(notebook, modelId, options)
        return notebook
