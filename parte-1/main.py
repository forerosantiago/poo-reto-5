"""
This code demonstrates the usage of the Shape module.

Usage:
- Import the Rectangle, Square, and Circle classes from the Shape.shapes module.
- Create instances of Rectangle, Square, and Circle with the desired dimensions.
- Use the compute_area() method to calculate the area of each shape.
- Use the compute_perimeter() method to calculate the perimeter of each shape.
- Print the results.

Example:


"""

from Shape.shapes import Rectangle, Square, Circle


rect = Rectangle(2, 3)
print(f"Area del rectángulo: {rect.compute_area()} unidades cuadradas")
print(f"Perímetro del rectángulo: {rect.compute_perimeter()} unidades")

sq = Square(2)
print(f"Area del cuadrado: {sq.compute_area()} unidades cuadradas")
print(f"Perímetro del cuadrado: {sq.compute_perimeter()} unidades")

circ = Circle(81)
print(f"Area del círculo: {circ.compute_area()} unidades cuadradas")
print(f"Perímetro del círculo: {circ.compute_perimeter()} unidades")
