class area:
    def __init__(self):
        self.ladoA = float(input("ingrese el valor de la variable A:"))
        self.ladoB = float(input("ingrese el valor de la variable B:"))
        self.ladoC = float(input("ingrese el valor de la variable C:"))

    def darAltura(self):
        altura = self.ladoA + self.ladoB
        return altura
    
    def darAreaTriangulo(self):
        areaTriangulo = (self.ladoB * self.darAltura()) / 2
        return areaTriangulo
    
    def darAreaRectangulo(self):
        areaRectangulo = self.ladoB * self.ladoC
        return areaRectangulo
    
    def areaTriangulo(self):
        areaTriangulo = self.darAreaRectangulo() + self.darAreaRectangulo()

solucion = area()

print ('el area del triangulo es:', solucion.areaTriangulo())

