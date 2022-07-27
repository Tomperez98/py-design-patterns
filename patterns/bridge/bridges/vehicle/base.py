from abc import abstractmethod
from dataclasses import dataclass

from patterns.bridge.strategies import IEngine


@dataclass
class BaseVehicle:
    engine: IEngine

    @abstractmethod
    def how_you_ride(self) -> str:
        pass
