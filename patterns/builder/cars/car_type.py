import enum


class CarType(str, enum.Enum):
    CITY_CAR = "CITY_CAR"
    SPORTS_CAR = "SPORTS_CAR"
    SUV = "SUV"
