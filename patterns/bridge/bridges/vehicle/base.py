from abc import abstractmethod
from dataclasses import dataclass

from patterns.bridge.strategies import IEngine


class BaseVehicle:
    def __init__(self, engine: IEngine) -> None:
        self.engine = engine

    @abstractmethod
    def how_you_ride(self) -> str:
        pass
