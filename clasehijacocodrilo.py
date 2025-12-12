from AnimalesAnderson import Animal
class Cocodrilo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)

    def moverse(self):
        return "Se arrastra por tierra y nada con facilidad en el agua."

    def comunicarse(self):
        return "Produce rugidos y sonidos profundos."

    def alimentarse(self):
        return "Se nutre de peces, aves y pequeños mamíferos."
    
AnimalCo = Cocodrilo("Cocodrilo", 7, "Río", "Carne", 200, "Verde")
AnimalCo.imprimir_datos()
print(AnimalCo.moverse())
print(AnimalCo.alimentarse())
print(AnimalCo.dormir())    
