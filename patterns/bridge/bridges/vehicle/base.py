from abc import ABC, abstractmethod
from dataclasses import dataclass

from patterns.bridge.strategies import IEngine


@dataclass
class BaseVehicleParamsMixin:
    engine: IEngine


class BaseVehicle(ABC, BaseVehicleParamsMixin):
    @abstractmethod
    def how_you_ride(self) -> str:
        pass
