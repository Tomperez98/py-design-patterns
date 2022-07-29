import enum

from patterns.factory_method.strategies import IShape, shapes


class ShapeFactory:
    class AvailableShapes(str, enum.Enum):
        SQUARE = "square"
        TRIANGLE = "triangle"
        CIRCLE = "circle"

    def create_shape(self, shape: str, **kwargs) -> IShape:

        if shape == self.AvailableShapes.SQUARE:
            return shapes.SquareShape(**kwargs)
        elif shape == self.AvailableShapes.CIRCLE:
            return shapes.CircleShape(**kwargs)
        elif shape == self.AvailableShapes.TRIANGLE:
            return shapes.TriangleShape(**kwargs)
        else:
            raise ValueError("Provided value not supported to be created")
