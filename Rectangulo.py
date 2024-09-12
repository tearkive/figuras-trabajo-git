class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura

# Ejemplo de uso
rectangulo = Rectangulo(5, 3)
print(f"El área del rectángulo es: {rectangulo.calcular_area()}")