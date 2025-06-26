from dataclasses import dataclass, asdict
from typing import Any, Dict


@dataclass
class ObjectModel:
    """
    Represents the outgoing payload structure for creating/updating an object via REST API.
    """
    id: int
    name: str
    data: Dict[str, Any]

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the dataclass to a dictionary for JSON serialization.
        """
        return asdict(self)


    # TODO: Refactor to a more structured model, for example:
    # @dataclass
    # class DeviceSpecs:
    #     brand: str
    #     color: str
    #     memory: str
    #
    # @dataclass
    # class ObjectModel:
    #     id: str
    #     name: str
    #     data: DeviceSpecs