from dataclasses import dataclass

from .base import BaseVehicle


@dataclass
class CarVehicle(BaseVehicle):
    def how_you_ride(self) -> str:
        return "4 wheeeeeeels"
