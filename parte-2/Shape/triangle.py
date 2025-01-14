"""A module for the Triangle class"""

from Shape.shape import Shape


class Triangle(Shape):
    """A triangle in a 2D space"""

    def __init__(self, side1, side2, side3):
        super().__init__()
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def compute_area(self):
        # Compute the area of the triangle using Heron's formula
        semiperimeter = self.compute_perimeter() / 2
        return (
            semiperimeter
            * (semiperimeter - self.side1)
            * (semiperimeter - self.side2)
            * (semiperimeter - self.side3)
        ) ** 0.5

    def compute_perimeter(self):
        return self.side1 + self.side2 + self.side3
