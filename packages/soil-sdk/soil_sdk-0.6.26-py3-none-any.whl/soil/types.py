"""Types used by soil library"""

# pylint:disable=unnecessary-ellipsis
from enum import Enum, StrEnum
from typing import Dict, List, Protocol, Self, Type, TypedDict

from soil.storage.base_storage import BaseStorage

Plan = List[Dict[str, str]]


class GetModule(TypedDict):
    """Type for GET modules/:moduleId"""

    is_package: bool
    public_api: List[str]
    package_type: str


class GetModuleHash(TypedDict):
    """Type for GET modules/"""

    name: str
    hash: str


class ExperimentStatuses(Enum):
    """Experiment Statuses"""

    WAITING = "WAITING"
    EXECUTING = "EXECUTING"
    DONE = "DONE"
    ERROR = "ERROR"


class Experiment(TypedDict):
    """Type for GET experiments/:experimentId"""

    _id: str
    app_id: str
    outputs: Dict[str, str]
    experiment_status: str


class Result(TypedDict):
    """Type for GET results/:resultId"""

    _id: str
    type: str


class _TypedDict(TypedDict):
    """Makes pyright happy"""

    pass


class SerializableDataStructure[Storage: BaseStorage, MetadataDict: _TypedDict](
    Protocol
):
    """Data Strucutre base protocol"""

    metadata: MetadataDict

    def serialize(self) -> Storage:
        """Serializes the DS."""
        ...

    @classmethod
    def deserialize(
        cls: Type[Self],
        storage: Storage,
        metadata: MetadataDict,
    ) -> "SerializableDataStructure[Storage, MetadataDict]":
        """Deserialize DS method."""
        ...


class TypeLog(StrEnum):
    """Types of Logs."""

    PROCESSED = "processed"
    NOT_CONSISTENT = "not_consistent"
    NOT_PROCESSED = "not_processed"
