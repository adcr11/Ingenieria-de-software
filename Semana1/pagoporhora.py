class pagoPorHora:
    def __init__(self):
        self.horasTrabajadas = float(input("dirigete el numero de horas trabajadas: "))
        self.pagoPorHora = float(input("dirigete el valor por hora:"))

    def calcularElSueldoSemana1(self):
        sueldoSemana1 = self.horasTrabajadas * self.pagoPorHora
        return sueldoSemana1
    
solucion = pagoPorHora()

print("recibe un sueldo de semana1 de:", solucion.calcularElSueldoSemana1())

