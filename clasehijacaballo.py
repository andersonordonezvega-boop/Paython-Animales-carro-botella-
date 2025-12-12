from AnimalesAnderson import Animal
class Caballo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)

    def moverse(self):
        return "El caballo avanza trotando o corriendo velozmente."

    def comunicarse(self):
        return "Se expresa mediante relinchos y gestos corporales."

    def reproducirse(self):
        return "La hembra da a luz a una cría tras casi un año de gestación."

    def alimentarse(self):
        return "Consume hierba, forraje y granos."

    def descansar(self):
        return "Duerme pocas horas, tanto de pie como recostado."
    
AnimalC = Caballo("Caballo", 5, "Pradera", "Hierba", 160, "Marrón")
AnimalC.imprimir_datos()
print(AnimalC.moverse())
print(AnimalC.alimentarse())
print(AnimalC.descansar())
