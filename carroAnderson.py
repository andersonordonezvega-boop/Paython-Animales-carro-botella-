# Clase padre


class Carro:
    
    def __init__(self, modelo, color, motor, puertas, capacidad, combustible):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.puertas = puertas
        self.capacidad = capacidad
        self.combustible = combustible

    def imprimir_datos(self):
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")
        print(f"Motor: {self.motor}")
        print(f"Puertas: {self.puertas}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Combustible: {self.combustible}")

   
    def arrancar(self):
        return("El vehículo ha iniciado su marcha correctamente.")

    def apagar(self):
        return("El vehículo se ha detenido y apagado correctamente.")

    def acelerar(self):
        return("El vehículo está acelerando.")

    def frenar(self):
        return("El sistema de frenos ha sido activado correctamente.")

    def direccional(self):
        return("Las luces direccionales están funcionando correctamente.")

    def luces(self):
        return("Las luces del vehículo están en buen estado.")

    def sistema_de_ventanas(self):
        return("Todas las ventanas están operando con normalidad.")

    def climatizacion(self):
        return("El sistema de climatización mantiene una temperatura confortable.")

    def sistema_de_espejos(self):
        return("Los espejos están ajustados para una visibilidad óptima.")

    def tipo_de_seguridad(self):
        return("El vehículo dispone de sistemas de seguridad avanzados.")


