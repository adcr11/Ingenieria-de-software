class precioPorGalon:
    def __init__(self):
        self.litrosProducidos = float(input("da la cantidad de litros: "))
        self.precioDeGalon = float(input("da el precio por galon: "))

    def calcularTotal(self):
        galonProducidos = self.litrosProducidos / 3.785
        total = galonProducidos * self.precioDeGalon
        return total
    
solucion = precioPorGalon()

print ("el productor ganara: ", solucion.calcularTotal())