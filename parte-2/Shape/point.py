"""This module contains the Point class"""

import math


class Point:
    """A point in a 2D space"""

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def compute_distance(self, other_point: "Point") -> float:
        """Compute the distance between two points"""
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
