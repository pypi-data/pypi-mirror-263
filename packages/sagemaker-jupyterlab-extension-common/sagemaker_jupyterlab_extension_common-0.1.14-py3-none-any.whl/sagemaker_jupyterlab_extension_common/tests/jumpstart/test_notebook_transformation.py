import json
import pytest
from sagemaker_jupyterlab_extension_common.jumpstart.notebook_transformation import (
    _get_substitue_cell,
    _is_cell_removal,
    _is_cell_replacement,
    _should_remove_cell,
    update_notebook,
)
from sagemaker_jupyterlab_extension_common.jumpstart.notebook_types import (
    JumpStartModelNotebookAlterationType,
    JumpStartModelNotebookGlobalActionType,
    JumpStartModelNotebookSubstitution,
    JumpStartModelNotebookSubstitutionTarget,
    UpdateHubNotebookUpdateOptions,
)


@pytest.mark.parametrize(
    "alteration_type,expected",
    [
        (JumpStartModelNotebookAlterationType.modelIdVersion, True),
        (JumpStartModelNotebookAlterationType.modelIdOnly, True),
        (JumpStartModelNotebookAlterationType.dropModelSelection, False),
        (JumpStartModelNotebookAlterationType.dropForDeploy, False),
        (JumpStartModelNotebookAlterationType.dropForTraining, False),
    ],
)
def test_is_cell_replacement(alteration_type, expected):
    assert expected == _is_cell_replacement(alteration_type)


@pytest.mark.parametrize(
    "alteration_type,expected",
    [
        (JumpStartModelNotebookAlterationType.modelIdVersion, False),
        (JumpStartModelNotebookAlterationType.modelIdOnly, False),
        (JumpStartModelNotebookAlterationType.dropModelSelection, True),
        (JumpStartModelNotebookAlterationType.dropForDeploy, True),
        (JumpStartModelNotebookAlterationType.dropForTraining, True),
    ],
)
def test_is_cell_removal(alteration_type, expected):
    assert expected == _is_cell_removal(alteration_type)


@pytest.mark.parametrize(
    "alteration_type,expected",
    [
        (JumpStartModelNotebookAlterationType.modelIdVersion.value, False),
        (JumpStartModelNotebookAlterationType.modelIdOnly.value, False),
        (JumpStartModelNotebookAlterationType.dropModelSelection.value, True),
        (JumpStartModelNotebookAlterationType.dropForDeploy.value, True),
        (JumpStartModelNotebookAlterationType.dropForTraining.value, True),
        (None, False),
        ("invalidType", False),
    ],
)
def test_should_remove_cell(alteration_type, expected):
    if alteration_type:
        cell = {"metadata": {"jumpStartAlterations": [f"{alteration_type}"]}}
    else:
        cell = {"metadata": {}}
    assert expected == _should_remove_cell(cell)


@pytest.mark.parametrize(
    "alteration_type,expected",
    [
        (
            JumpStartModelNotebookAlterationType.modelIdVersion.value,
            ['model_id, model_version = "test_model_id", "*"'],
        ),
        (
            JumpStartModelNotebookAlterationType.modelIdOnly.value,
            ['model_id = "test_model_id"'],
        ),
        (
            None,
            [],
        ),
    ],
)
def test_get_substitue_cell(alteration_type, expected):
    model_id = "test_model_id"
    if alteration_type:
        current_cell = {
            "metadata": {"jumpStartAlterations": [f"{alteration_type}"]},
            "source": [],
        }
    else:
        current_cell = {"metadata": {}, "source": []}
    assert expected == _get_substitue_cell(model_id, current_cell)["source"]


@pytest.mark.parametrize(
    "content,error_message",
    [
        ("invalid_json_content", "Notebook is not a valid JSON"),
        ("{}", "Notebook validation failed"),
    ],
)
def test_update_notebook_with_invalid_notebook(content, error_message):
    options = UpdateHubNotebookUpdateOptions([], [], [])
    with pytest.raises(ValueError, match=error_message):
        update_notebook(content, None, options)


def test_update_notebook_with_valid_notebook():
    options = UpdateHubNotebookUpdateOptions([], [], [])
    content = {
        "cells": [],
        "metadata": {
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.8.13",
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    content_str = json.dumps(content)
    assert content_str == update_notebook(content_str, None, options)


def test_update_notebook_with_drop_cell_operation():
    alterations = [
        JumpStartModelNotebookAlterationType.dropModelSelection,
    ]
    options = UpdateHubNotebookUpdateOptions([], alterations, [])
    content = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {"jumpStartAlterations": ["dropModelSelection"]},
                "source": ["content"],
            }
        ],
        "metadata": {
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.8.13",
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    content_str = json.dumps(content)
    assert 0 == len(json.loads(update_notebook(content_str, None, options))["cells"])


def test_update_notebook_with_model_id_substitution():
    alterations = [
        JumpStartModelNotebookAlterationType.modelIdOnly,
    ]
    options = UpdateHubNotebookUpdateOptions([], alterations, [])
    content = {
        "cells": [
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {"jumpStartAlterations": ["modelIdOnly"]},
                "source": ["content"],
                "outputs": [],
            }
        ],
        "metadata": {
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.8.13",
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    content_str = json.dumps(content)
    assert ['model_id = "mock_model_id"'] == json.loads(
        update_notebook(content_str, "mock_model_id", options)
    )["cells"][0]["source"]


def test_update_notebook_with_model_version_substitution():
    alterations = [
        JumpStartModelNotebookAlterationType.modelIdVersion,
    ]
    options = UpdateHubNotebookUpdateOptions([], alterations, [])
    content = {
        "cells": [
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {"jumpStartAlterations": ["modelIdVersion"]},
                "source": ["content"],
                "outputs": [],
            }
        ],
        "metadata": {
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.8.13",
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    content_str = json.dumps(content)
    assert ['model_id, model_version = "mock_model_id", "*"'] == json.loads(
        update_notebook(content_str, "mock_model_id", options)
    )["cells"][0]["source"]


def test_update_notebook_with_global_drop_markdow():
    globalActions = [
        JumpStartModelNotebookGlobalActionType.dropAllMarkdown,
    ]
    options = UpdateHubNotebookUpdateOptions([], [], globalActions)
    content = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {"jumpStartAlterations": ["dropAllMarkdown"]},
                "source": ["content"],
            }
        ],
        "metadata": {
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.8.13",
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    content_str = json.dumps(content)
    assert 0 == len(json.loads(update_notebook(content_str, None, options))["cells"])


def test_update_notebook_with_endpoint_name_substitution():
    substitutions = [
        JumpStartModelNotebookSubstitution(
            JumpStartModelNotebookSubstitutionTarget.endpointName,
            "mock-endpoint-name",
            True,
        ),
        JumpStartModelNotebookSubstitution(
            JumpStartModelNotebookSubstitutionTarget.inferenceComponentTarget,
            "mock-inference-component-name",
            True,
        ),
    ]
    options = UpdateHubNotebookUpdateOptions(substitutions, [], [])
    content = {
        "cells": [
            {
                "cell_type": "code",
                "execution_count": None,
                "source": ["endpointName=!!!name!!!"],
                "metadata": {},
                "outputs": [],
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "source": ["EndpointName=endpoint_name"],
                "metadata": {},
                "outputs": [],
            },
        ],
        "metadata": {
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.8.13",
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    content_str = json.dumps(content)
    result = json.loads(update_notebook(content_str, None, options))
    assert "endpointName=mock-endpoint-name" == result["cells"][0]["source"][0]
    assert "mock-inference-component-name" == result["cells"][1]["source"][0]
