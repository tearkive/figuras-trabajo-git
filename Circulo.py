class Circulo:
    def __init__(self,radio):
        self.radio = radio
    
    def calcular_area(self):
        return (self.radio)^2*3.1416

#Ejemplo de uso
circulo = Circulo(3)