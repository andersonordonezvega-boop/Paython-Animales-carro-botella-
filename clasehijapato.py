from AnimalesAnderson import Animal
class Pato(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)

    def moverse(self):
        return "Camina por tierra, nada y vuela distancias cortas."

    def comunicarse(self):
        return "Emite sonidos característicos como graznidos."

    def alimentarse(self):
        return "Su dieta incluye semillas, insectos y vegetales acuáticos."



AnimalPa = Pato("Pato", 4, "Lago", "Semillas y peces", 0.45, "Blanco y verde")
AnimalPa.imprimir_datos()
print(AnimalPa.moverse())
print(AnimalPa.comunicarse())
print(AnimalPa.interactuar_socialmente())
