from __future__ import annotations

import dataclasses

from patterns.builder import cars


@dataclasses.dataclass
class TripComputer:
    car: cars.Car = dataclasses.field(init=False)

    def show_fuel_level(self) -> str:
        return f"Fuel level: {self.car.fuel}"

    def show_status(self) -> str:
        if self.car.engine.is_started():
            return "Car is started"
        else:
            return "Car is not started"
