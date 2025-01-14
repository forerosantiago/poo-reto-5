"""This module defines the Shape class"""


class Shape:
    """A generic shape in a 2D space"""

    def __init__(self):
        pass

    def compute_area(self) -> float:
        """Compute the area of the shape"""
        raise NotImplementedError("Subclasses should implement this method")

    def compute_perimeter(self) -> float:
        """Compute the perimeter of the shape"""
        raise NotImplementedError("Subclasses should implement this method")
