from AnimalesAnderson import Animal
class Pez(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)

    def moverse(self):
        return "Nada moviendo las aletas y su cola."

    def comunicarse(self):
        return "Se comunica con movimientos y cambios de color."

    def alimentarse(self):
        return "Come plancton o peces diminutos, según la especie."


AnimalP = Pez("Pez Ángel", 3, "Océano", "Plancton", 0.20, "Azul")
AnimalP.imprimir_datos()
print(AnimalP.moverse())
print(AnimalP.alimentarse())
print(AnimalP.descansar())
