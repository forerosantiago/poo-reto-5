"""This module defines the Square class"""

from rectangle import Rectangle


class Square(Rectangle):
    """A square in a 2D space"""

    def __init__(self, side):
        super().__init__(side, side)
