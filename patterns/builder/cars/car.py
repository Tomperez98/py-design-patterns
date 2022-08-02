"""
Car is a product Class
"""
from __future__ import annotations

import dataclasses
import decimal

from patterns.builder import components

from .car_type import CarType


@dataclasses.dataclass
class Car:
    car_type: CarType
    seats: int
    engine: components.Engine
    transmission: components.Transmission
    trip_computer: components.TripComputer
    gps_navigator: components.GPSNavigator
    fuel: decimal.Decimal = dataclasses.field(
        init=False, default=decimal.Decimal(0)
    )

    def __post_init__(self) -> None:
        if self.trip_computer:
            self.trip_computer.car = self
