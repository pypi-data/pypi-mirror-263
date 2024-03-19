from dataclasses import dataclass
from enum import Enum
from typing import List


class JumpStartBucketStage(Enum):
    PROD = ("prod",)
    BETA = ("beta",)
    ALPHA = ("alpha",)
    GAMMA = ("gamma",)
    SBX = ("sbx",)


class JumpStartModelNotebookAlterationType(Enum):
    modelIdVersion = "modelIdVersion"
    modelIdOnly = "modelIdOnly"
    dropModelSelection = "dropModelSelection"
    dropForDeploy = "dropForDeploy"
    dropForTraining = "dropForTraining"


class JumpStartNotebookNames(Enum):
    infer = "inference"
    train = "training"


class JumpStartModelNotebookSubstitutionTarget(Enum):
    endpointName = "endpointName"
    inferenceComponentTarget = "inferenceComponentTarget"


class JumpStartResourceType(Enum):
    inferNotebook = "inferNotebook"
    modelSdkNotebook = "modelSdkNotebook"
    proprietaryNotebook = "proprietaryNotebook"
    default = "notebook"


class JumpStartModelNotebookGlobalActionType(Enum):
    dropAllMarkdown = "dropAllMarkdown"
    dropAllCode = "dropAllCode"


class JumpStartModelNotebookSubstitutionTarget(Enum):
    endpointName = "!!!name!!!"
    inferenceComponentTarget = "EndpointName=endpoint_name"


class JumpStartModelNotebookSuffix(Enum):
    modelSdkNotebook = "sdk"
    inferNotebook = "infer"
    proprietaryNotebook = "pp"


@dataclass
class JumpStartModelNotebookSubstitution:
    find: JumpStartModelNotebookSubstitutionTarget
    replace: str
    onlyOnce: bool


@dataclass
class UpdateHubNotebookUpdateOptions:
    substitutions: List[JumpStartModelNotebookSubstitution]
    alterations: List[JumpStartModelNotebookAlterationType]
    globalActions: List[JumpStartModelNotebookGlobalActionType]
