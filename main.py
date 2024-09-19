from Rectangulo import Rectangulo
from Circulo import Circulo
from Triangulo import Triangulo
from Cuadrado import Cuadrado

figuras = []

triangulo = Triangulo(10, 5)
cuadrado = Cuadrado(4)
rectangulo = Rectangulo(6, 3)
circulo = Circulo(7)

figuras.append(triangulo)
figuras.append(cuadrado)
figuras.append(rectangulo)
figuras.append(circulo)

for figura in figuras:
    print(f"El área del {type(figura).__name__} es: {figura.calcular_area()}")