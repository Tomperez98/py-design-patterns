"""
Car manual is another product. Note that it does not have the same
ancestor as a Car. They are not related.
"""
from __future__ import annotations

import dataclasses

from patterns.builder import components

from .car_type import CarType


@dataclasses.dataclass
class Manual:
    car_type: CarType
    seats: int
    engine: components.Engine
    transmission: components.Transmission
    trip_computer: components.TripComputer
    gps_navigator: components.GPSNavigator

    def show(self) -> str:
        info = ""
        info += f"Type of car: {self.car_type} \n"
        info += f"Number of seats: {self.seats} \n"
        info += (
            f"Engine volume - {self.engine.volume};"
            " mileage {self.engine.get_mileage()} \n"
        )
        info += "Trip computer: Functional \n"
        info += "GPS navigator: Functional \n"
        return info
