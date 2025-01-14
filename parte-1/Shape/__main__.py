""""This is the Shape package. It defines the Point, Line and Shape classes and its subclasses"""

import math


class Point:
    """A point in a 2D space"""

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def compute_distance(self, other_point: "Point") -> float:
        """Compute the distance between two points"""
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


class Line:
    """A line in a 2D space"""

    def __init__(self, start_point: "Point", end_point: "Point"):
        self.start_point = start_point
        self.end_point = end_point
        self.length = self.compute_length()

    def compute_length(self) -> float:
        """Compute the length of the line"""
        return self.start_point.compute_distance(self.end_point)


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


class Square(Rectangle):
    """A square in a 2D space"""

    def __init__(self, side):
        super().__init__(side, side)


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


class Circle(Shape):
    """A circle in a 2D space"""

    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def compute_area(self):
        return math.pi * self.radius**2

    def compute_perimeter(self):
        return 2 * math.pi * self.radius

# Usage example
if __name__ == "__main__":
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    print(f"Distancia entre P1 y P2: {p1.compute_distance(p2)} unidades")

    linea = Line(p1, p2)
    print(f"Longitud del segmento P1P2: {linea.length} unidades")

    r = Rectangle(3, 4)
    print(f"Area del rectángulo r: {r.compute_area()} unidades cuadradas")
    print(f"Perímetro del rectángulo r: {r.compute_perimeter()} unidades")

    s = Square(3)
    print(f"Area del cuadrado s: {s.compute_area()} unidades cuadradas")
    print(f"Perímetro del cuadrado s: {s.compute_perimeter()} unidades")

    t = Triangle(3, 4, 5)
    print(f"Área del triángulo t: {t.compute_area()} unidades cuadradas")
    print(f"Perímetro del triángulo t: {t.compute_perimeter()}")

    c = Circle(5)
    print(f"Área del círculo c: {c.compute_area()} unidades cuadradas")
    print(f"Perímetro del círculo c: {c.compute_perimeter()} unidades")
