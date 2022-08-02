import decimal

from patterns import builder
from patterns.builder import cars, components


def test_pattern():
    director = builder.Director()

    car_builder = builder.CarBuilder()

    director.build_sports_car(builder=car_builder)

    created_car = car_builder.receive_car()
    assert created_car.car_type == cars.CarType.SPORTS_CAR
