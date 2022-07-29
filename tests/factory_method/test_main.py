from decimal import Decimal
from typing import Dict, Type

import pytest

from patterns import factory_method
from patterns.factory_method.strategies import IShape, shapes


@pytest.mark.parametrize(
    "shape, payload, expected_type",
    [
        (
            "square",
            {
                "side": Decimal(10),
            },
            shapes.SquareShape,
        ),
        (
            "triangle",
            {
                "base": Decimal(10),
                "height": Decimal(5),
            },
            shapes.TriangleShape,
        ),
        (
            "circle",
            {
                "radius": Decimal(3),
            },
            shapes.CircleShape,
        ),
    ],
)
def test_pattern(
    shape: str, payload: Dict[str, Decimal], expected_type: Type[IShape]
):
    factory = factory_method.ShapeFactory()
    generated_shape = factory.create_shape(shape=shape, **payload)
    assert isinstance(generated_shape, expected_type)


def test_no_available_value():
    factory = factory_method.ShapeFactory()
    with pytest.raises(ValueError):
        factory.create_shape(shape="not a shape")
