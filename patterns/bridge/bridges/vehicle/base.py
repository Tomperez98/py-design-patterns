from abc import ABC, abstractmethod
from dataclasses import dataclass

from patterns.bridge.strategies import IEngine


@dataclass
class BaseVehicleMixin:
    engine: IEngine


class BaseVehicle(ABC, BaseVehicleMixin):
    @abstractmethod
    def how_you_ride(self) -> str:
        pass
