from dataclasses import dataclass

from .base import BaseVehicle


@dataclass
class MotorcycleVehicle(BaseVehicle):
    def how_you_ride(self) -> str:
        return "2 wheels but fast"
