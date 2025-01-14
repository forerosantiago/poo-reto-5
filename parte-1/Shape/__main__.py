"""Demonstrates the usage of the shapes module"""

from shapes import Point, Line, Rectangle, Square, Triangle, Circle

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
