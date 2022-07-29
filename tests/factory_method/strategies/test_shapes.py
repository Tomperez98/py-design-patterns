from decimal import Decimal

import pytest

from patterns.factory_method.strategies import IShape, shapes


@pytest.mark.parametrize(
    "shape, expected_area",
    [
        (
            shapes.CircleShape(radius=Decimal(10)),
            Decimal(314.16),
        ),
        (
            shapes.SquareShape(side=Decimal(10)),
            Decimal(100),
        ),
        (
            shapes.TriangleShape(base=Decimal(5), height=Decimal(7)),
            Decimal(17.5),
        ),
    ],
)
def test_shapes(
    shape: IShape,
    expected_area: Decimal,
):
    assert pytest.approx(shape.area(), rel=Decimal(0.1)) == expected_area
