"""Module defining the Line class"""

from .point import Point


class Line:
    """A line in a 2D space"""

    def __init__(self, start_point: "Point", end_point: "Point"):
        self.start_point = start_point
        self.end_point = end_point
        self.length = self.compute_length()

    def compute_length(self) -> float:
        """Compute the length of the line"""
        return self.start_point.compute_distance(self.end_point)
