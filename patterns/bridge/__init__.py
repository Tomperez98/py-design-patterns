from .bridges import BaseVehicle
from .bridges.vehicle import AirplaneVehicle, CarVehicle, MotorcycleVehicle
from .strategies import IEngine
from .strategies.engines import ElectricEngine, GasolineEngine

__all__ = [
    "BaseVehicle",
    "AirplaneVehicle",
    "CarVehicle",
    "MotorcycleVehicle",
    "IEngine",
    "ElectricEngine",
    "GasolineEngine",
]
