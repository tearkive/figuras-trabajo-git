class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        self.area = 0

    def calcular_area(self):
        self.area = 0.5 * self.base * self.altura
        return self.area
    
    def desplegar_area(self):
        print(f"El área del triángulo es: {self.area}")

triangulo = Triangulo(10, 5)
area = triangulo.calcular_area()
triangulo.desplegar_area()