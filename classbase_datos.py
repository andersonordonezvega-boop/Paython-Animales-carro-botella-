class base_datos:
    def __init__(self):
        self.lista_dato = []

    def agregar_animal(self, animal):
        self.lista_dato.append(animal)
        print("Animal agregado:", self.lista_dato)

    def agregar_animales_de_otra_lista(self, lista_nueva):
        self.lista_dato.extend(lista_nueva)
        print("Se agregaron los animales de la otra lista:")
        print(self.lista_dato)

    def insertar_animal_posicion_especifica(self, posicion, animal_nuevo):
        self.lista_dato.insert(posicion, animal_nuevo)
        print("Lista actual:", self.lista_dato)

    def eliminar_primer_animal(self, nombre):
        if nombre in self.lista_dato:
            self.lista_dato.remove(nombre)
            print(f"Se eliminó '{nombre}' de la lista")
        else:
            print("Ese animal no está en la lista")

    def buscar_posicion(self, nombre):
        if nombre in self.lista_dato:
            print(f"{nombre} está en la posición {self.lista_dato.index(nombre)}")
        else:
            print("No se encontró ese animal")

    def contar_animal(self, nombre):
        print(f"{nombre} aparece {self.lista_dato.count(nombre)} veces")

    def ordenar_animales(self):
        self.lista_dato.sort()
        print("Lista ordenada:", self.lista_dato)

    def invertir_orden_de_los_elementos(self):
        self.lista_dato.reverse()
        print("Lista invertida:", self.lista_dato)


# --- Ejemplo de uso ---
bd = base_datos()
bd.agregar_animal("escarabajo")
bd.agregar_animales_de_otra_lista(["perro", "gato"])
bd.insertar_animal_posicion_especifica(2, "cocodrilo")
bd.eliminar_primer_animal("escarabajo")
bd.buscar_posicion("cocodrilo")
bd.contar_animal("cocodrilo")
bd.ordenar_animales()
bd.invertir_orden_de_los_elementos()
