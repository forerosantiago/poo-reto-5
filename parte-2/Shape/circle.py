"""This module provides a Circle class"""

import math

from shape import Shape


class Circle(Shape):
    """A circle in a 2D space"""

    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def compute_area(self):
        return math.pi * self.radius**2

    def compute_perimeter(self):
        return 2 * math.pi * self.radius
