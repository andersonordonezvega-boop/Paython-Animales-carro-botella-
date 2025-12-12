class base_datos:
    def __init__(self):
        self.lista_datos = []

    def agregar_elemento(self, botella_nueva):
        self.lista_datos.append(botella_nueva)
        print(self.lista_datos)

    def agregar_elementos_otra_lista(self, lista_nueva):
        self.lista_datos.extend(lista_nueva)
        print(self.lista_datos)

    def insertar_elemento_posicion_especifica(self, posicion, objeto_nuevo):
        self.lista_datos.insert(posicion, objeto_nuevo)
        print(self.lista_datos)

    def eliminar_primer_elemento(self, valor):
        if valor in self.lista_datos:
            self.lista_datos.remove(valor)
            print(f"Se eliminó '{valor}'")
        else:
            print("Esa botella no está en la lista")

    def buscar_posicion(self, valor):
        if valor in self.lista_datos:
            print(f"{valor} está en la posición {self.lista_datos.index(valor)}")
        else:
            print("No se encontró esa botella")

    def contar_botella(self, valor):
        print(f"{valor} aparece {self.lista_datos.count(valor)} veces")

    def ordenar_botellas(self):
        self.lista_datos.sort()
        print("Lista ordenada:", self.lista_datos)

    def invertir_orden_de_los_elementos(self):
        self.lista_datos.reverse()
        print("Lista invertida:", self.lista_datos)



bd = base_datos()

bd.agregar_elemento("botella roja")
bd.agregar_elementos_otra_lista(["botella azul", "botella amarilla"])
bd.insertar_elemento_posicion_especifica(2, "botella verde")
bd.eliminar_primer_elemento("botella amarilla")
bd.buscar_posicion("botella azul")
bd.contar_botella("botella roja")
bd.ordenar_botellas()
bd.invertir_orden_de_los_elementos()

