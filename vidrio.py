from BotellaAnderson import Botellapadre
class BotellaVidrio(Botellapadre):
    def __init__(self, material, capacidad, forma, diseño, tapa, grabados):
        super().__init__(material, capacidad, forma, diseño, tapa, grabados)

  

def Contener_liquidos(self):
    print("las botellas almacenan diferentes tipos de bebidas\n")

def Facilitar_vertido(self):
    print("el diseño de la botella permite verter el contenido con facilidad\n")

def Cierre_hermetico(self):
    print("la tapa se ajusta firmemente para evitar fugas o derrames\n")

def Transporte_botellas(self):
    print("las botellas pueden transportarse fácilmente en cajas o vehículos\n")

def Manejar_botellas(self):
    print("deben manipularse con precaución para evitar daños o roturas\n")

def Compatibilidad_bebidas_calientes_frias(self):
    print("son aptas para contener líquidos tanto fríos como calientes\n")

def Reutilizacion_envase(self):
    print("el envase puede usarse nuevamente después de su limpieza\n")

def Transparencia_botelle(self):
    print("la mayoría de las botellas permiten ver el contenido en su interior\n")

# Código principal




botellav = BotellaVidrio("vidrio", 750, "rectangular", "clásico", "corcho", "florales")
botellav.imprimir_datos()
print(botellav.contener_liquidos())
print(botellav.facilitar_el_vertido())
print(botellav.cierre_hermetico())
print(botellav.transporte())
print(botellav.manejo())
print(botellav.compatibilidad_bebidas())
print(botellav.reutilizacion())
print(botellav.transparencia())
