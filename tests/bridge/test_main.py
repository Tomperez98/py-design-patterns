from typing import List, Type

import pytest

from patterns import bridge
from patterns.bridge.strategies.engines.interface import IEngine


@pytest.mark.parametrize(
    "vehicle_type, engine_type, expected_responses",
    [
        (
            bridge.MotorcycleVehicle,
            bridge.ElectricEngine,
            [
                "Charged in an hour",
                "2 wheels but fast",
            ],
        ),
        (
            bridge.CarVehicle,
            bridge.ElectricEngine,
            [
                "Charged in an hour",
                "4 wheeeeeeels",
            ],
        ),
        (
            bridge.AirplaneVehicle,
            bridge.GasolineEngine,
            [
                "The fuel is so expensive",
                "Ride? No, I fly",
            ],
        ),
    ],
)
def test_pattern(
    vehicle_type: Type[bridge.BaseVehicle],
    engine_type: Type[IEngine],
    expected_responses: List[str],
):
    created_vehicle = vehicle_type(engine=engine_type())
    assert created_vehicle.engine.charge_engine() == expected_responses[0]
    assert created_vehicle.how_you_ride() == expected_responses[1]
