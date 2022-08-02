import decimal

from patterns.builder import builders, cars, components


class Director:
    def build_sports_car(self, builder: builders.IBuilder) -> None:
        builder.set_car_type(car_type=cars.CarType.SPORTS_CAR)
        builder.set_seats(seats=2)
        builder.set_engine(
            engine=components.Engine(
                volume=decimal.Decimal(3.0), mileage=decimal.Decimal(0)
            )
        )
        builder.set_transmission(
            transmission=components.Transmission.SEMI_AUTOMATIC
        )
        builder.set_trip_computer(trip_computer=components.TripComputer())
        builder.set_gps_navigator(gps_navigator=components.GPSNavigator())

    def build_city_car(self, builder: builders.IBuilder) -> None:
        builder.set_car_type(car_type=cars.CarType.CITY_CAR)
        builder.set_seats(seats=2)
        builder.set_engine(
            engine=components.Engine(
                volume=decimal.Decimal(1.2), mileage=decimal.Decimal(0)
            )
        )
        builder.set_transmission(
            transmission=components.Transmission.AUTOMATIC
        )
        builder.set_trip_computer(trip_computer=components.TripComputer())
        builder.set_gps_navigator(gps_navigator=components.GPSNavigator())

    def build_suv(self, builder: builders.IBuilder) -> None:
        builder.set_car_type(car_type=cars.CarType.SUV)
        builder.set_seats(seats=4)
        builder.set_engine(
            engine=components.Engine(
                volume=decimal.Decimal(2.5), mileage=decimal.Decimal(0)
            )
        )
        builder.set_transmission(transmission=components.Transmission.MANUAL)
        builder.set_gps_navigator(gps_navigator=components.GPSNavigator())
