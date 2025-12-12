class Animal:
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamaño = tamaño
        self.color = color

    def imprimir_datos(self):
        print(f"\nNombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Hábitat: {self.habitat}")
        print(f"Dieta: {self.dieta}")
        print(f"Tamaño: {self.tamaño}")
        print(f"Color: {self.color}")

    def moverse(self):
        return "El animal se desplaza por su entorno."

    def comunicarse(self):
        return "El animal transmite señales o sonidos a otros."

    def reproducirse(self):
        return "El animal está en proceso de reproducción."

    def alimentarse(self):
        return "El animal ingiere su alimento."

    def descansar(self):
        return "El animal toma un tiempo de reposo."

    def dormir(self):
        return "El animal se encuentra dormido."

    def interactuar_socialmente(self):
        return "El animal se relaciona con los de su grupo."


# Clases hijas
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


class Cocodrilo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)

    def moverse(self):
        return "Se arrastra por tierra y nada con facilidad en el agua."

    def comunicarse(self):
        return "Produce rugidos y sonidos profundos."

    def alimentarse(self):
        return "Se nutre de peces, aves y pequeños mamíferos."


class Pez(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)

    def moverse(self):
        return "Nada moviendo las aletas y su cola."

    def comunicarse(self):
        return "Se comunica con movimientos y cambios de color."

    def alimentarse(self):
        return "Come plancton o peces diminutos, según la especie."


class Escarabajo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)

    def moverse(self):
        return "Camina lentamente o utiliza sus alas para volar."

    def comunicarse(self):
        return "Usa feromonas y vibraciones para enviar señales."

    def alimentarse(self):
        return "Consume hojas, madera o restos de materia vegetal."


class Pato(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)

    def moverse(self):
        return "Camina por tierra, nada y vuela distancias cortas."

    def comunicarse(self):
        return "Emite sonidos característicos como graznidos."

    def alimentarse(self):
        return "Su dieta incluye semillas, insectos y vegetales acuáticos."


# Código principal
AnimalC = Caballo("Caballo", 5, "Pradera", "Hierba", 160, "Marrón")
AnimalC.imprimir_datos()
print(AnimalC.moverse())
print(AnimalC.alimentarse())
print(AnimalC.descansar())

AnimalCo = Cocodrilo("Cocodrilo", 7, "Río", "Carne", 200, "Verde")
AnimalCo.imprimir_datos()
print(AnimalCo.moverse())
print(AnimalCo.alimentarse())
print(AnimalCo.dormir())

AnimalP = Pez("Pez Ángel", 3, "Océano", "Plancton", 0.20, "Azul")
AnimalP.imprimir_datos()
print(AnimalP.moverse())
print(AnimalP.alimentarse())
print(AnimalP.descansar())

AnimalE = Escarabajo("Escarabajo Rinoceronte", 1, "Bosque", "Hojas", 0.5, "Negro brillante")
AnimalE.imprimir_datos()
print(AnimalE.moverse())
print(AnimalE.reproducirse())

AnimalPa = Pato("Pato", 4, "Lago", "Semillas y peces", 0.45, "Blanco y verde")
AnimalPa.imprimir_datos()
print(AnimalPa.moverse())
print(AnimalPa.comunicarse())
print(AnimalPa.interactuar_socialmente())
