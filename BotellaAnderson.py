class Botellapadre:
    
    def __init__(self, material, capacidad, forma, diseño, tapa, grabados):
        self.material = material
        self.capacidad = capacidad
        self.forma = forma
        self.diseño = diseño
        self.tapa = tapa
        self.grabados = grabados

    def imprimir_datos(self):
        print(f"Material: {self.material}")
        print(f"Capacidad: {self.capacidad} ml")
        print(f"Forma: {self.forma}")
        print(f"Diseño: {self.diseño}")
        print(f"Tapa: {self.tapa}")
        print(f"Grabados: {self.grabados}")

    
    def contener_liquidos(self):
        return "Sirve para guardar distintos tipos de líquidos."

    def facilitar_el_vertido(self):
        return "Su estructura permite verter el contenido con facilidad."

    def cierre_hermetico(self):
        return "Posee un cierre seguro que impide filtraciones."

    def transporte(self):
        return "Puede transportarse sin dificultad debido a su tamaño y peso."

    def manejo(self):
        return "Es cómoda de usar y sostener."

    def compatibilidad_bebidas(self):
        return "Apta para conservar bebidas tanto frías como calientes."

    def reutilizacion(self):
        return "Puede ser usada en múltiples ocasiones sin perder calidad."

    def transparencia(self):
        return "Su material permite observar el contenido interior."




