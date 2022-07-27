from dataclasses import dataclass

from .base import BaseVehicle


@dataclass
class AirplaneVehicle(BaseVehicle):
    def how_you_ride(self) -> str:
        return "Ride? No, I fly"
