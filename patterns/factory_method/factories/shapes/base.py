import enum

from patterns.factory_method.strategies import IShape, shapes


class ShapeFactory:
    class AvailableShapes(str, enum.Enum):
        SQUARE = "square"
        TRIANGLE = "triangle"
        CIRCLE = "circle"

    @classmethod
    def create_shape(cls, shape: str, **kwargs) -> IShape:

        if shape == cls.AvailableShapes.SQUARE:
            return shapes.SquareShape(**kwargs)
        elif shape == cls.AvailableShapes.CIRCLE:
            return shapes.CircleShape(**kwargs)
        elif shape == cls.AvailableShapes.TRIANGLE:
            return shapes.TriangleShape(**kwargs)
        else:
            raise ValueError("Provided value not supported to be created")
