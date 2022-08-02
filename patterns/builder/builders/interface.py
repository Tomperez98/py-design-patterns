from __future__ import annotations

import abc

from patterns.builder import cars, components


class IBuilder(abc.ABC):
    @abc.abstractmethod
    def set_car_type(self, car_type: cars.CarType) -> None:
        pass

    @abc.abstractmethod
    def set_seats(self, seats: int) -> None:
        pass

    @abc.abstractmethod
    def set_engine(self, engine: components.Engine) -> None:
        pass

    @abc.abstractmethod
    def set_transmission(self, transmission: components.Transmission) -> None:
        pass

    @abc.abstractmethod
    def set_trip_computer(
        self, trip_computer: components.TripComputer
    ) -> None:
        pass

    @abc.abstractmethod
    def set_gps_navigator(
        self, gps_navigator: components.GPSNavigator
    ) -> None:
        pass
