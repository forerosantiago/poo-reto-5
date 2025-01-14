from Shape import rectangle, square, circle

rectangle = Rectangle(2, 3)
print(f"Area del rectángulo: {rectangle.compute_area()} unidades cuadradas")
print(f"Perímetro del rectángulo: {rectangle.compute_perimeter()} unidades")

square = Square(2)
print(f"Area del cuadrado: {square.compute_area()} unidades cuadradas")
print(f"Perímetro del cuadrado: {square.compute_perimeter()} unidades")

circle = Circle(81)
print(f"Area del círculo: {circle.compute_area()} unidades cuadradas")
print(f"Perímetro del círculo: {circle.compute_perimeter()} unidades")
