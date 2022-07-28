from abc import ABC, abstractmethod
from dataclasses import dataclass

from patterns.bridge.strategies import IEngine


class BaseVehicleMethods(ABC):
    @abstractmethod
    def how_you_ride(self) -> str:
        pass


@dataclass
class BaseVehicleParams:
    engine: IEngine


class BaseVehicle(BaseVehicleMethods, BaseVehicleParams):
    pass
