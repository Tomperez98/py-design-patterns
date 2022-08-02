import dataclasses

from patterns.builder import cars, components
from patterns.builder.builders import interface


@dataclasses.dataclass(init=False)
class CarBuilder(interface.IBuilder):
    car_type: cars.CarType
    seats: int
    engine: components.Engine
    transmission: components.Transmission
    trip_computer: components.TripComputer
    gps_navigator: components.GPSNavigator

    def set_car_type(self, car_type: cars.CarType) -> None:
        self.car_type = car_type

    def set_seats(self, seats: int) -> None:
        self.seats = seats

    def set_engine(self, engine: components.Engine) -> None:
        self.engine = engine

    def set_transmission(self, transmission: components.Transmission) -> None:
        self.transmission = transmission

    def set_trip_computer(
        self, trip_computer: components.TripComputer
    ) -> None:
        self.trip_computer = trip_computer

    def set_gps_navigator(
        self, gps_navigator: components.GPSNavigator
    ) -> None:
        self.gps_navigator = gps_navigator

    def receive_car(self) -> cars.Car:
        return cars.Car(
            car_type=self.car_type,
            seats=self.seats,
            engine=self.engine,
            transmission=self.transmission,
            trip_computer=self.trip_computer,
            gps_navigator=self.gps_navigator,
        )
