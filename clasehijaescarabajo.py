from AnimalesAnderson import Animal
class Escarabajo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)

    def moverse(self):
        return "Camina lentamente o utiliza sus alas para volar."

    def comunicarse(self):
        return "Usa feromonas y vibraciones para enviar señales."

    def alimentarse(self):
        return "Consume hojas, madera o restos de materia vegetal."



AnimalE = Escarabajo("Escarabajo Rinoceronte", 1, "Bosque", "Hojas", 0.5, "Negro brillante")
AnimalE.imprimir_datos()
print(AnimalE.moverse())
print(AnimalE.reproducirse())