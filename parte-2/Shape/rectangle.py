"""Rectangle class"""

from Shape.shape import Shape


class Rectangle(Shape):
    """A rectangle in a 2D space"""

    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def compute_area(self) -> float:
        return self.width * self.height

    def compute_perimeter(self) -> float:
        return 2 * (self.width + self.height)
