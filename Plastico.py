from BotellaAnderson import Botellapadre
class BotellaPlastica(Botellapadre):
    def __init__(self, material, capacidad, forma, diseño, tapa, grabados):
        super().__init__(material, capacidad, forma, diseño, tapa, grabados)

    # Métodos específicos de la botella plástica
def Contener_liquidos(self):
    print("las botellas sirven para guardar distintos líquidos o bebidas\n")

def Facilitar_vertido(self):
    print("su estructura está diseñada para verter el contenido sin dificultad\n")

def Cierre_hermetico(self):
    print("la tapa asegura un sellado completo para conservar el producto\n")

def Transporte_botellas(self):
    print("las botellas se transportan de forma segura en empaques o camiones\n")

def Manejar_botellas(self):
    print("es importante manipularlas con cuidado para evitar derrames o daños\n")

def Compatibilidad_bebidas_calientes_frias(self):
    print("pueden contener bebidas a diferentes temperaturas sin deformarse\n")

def Reutilizacion_envase(self):
    print("puede lavarse y usarse nuevamente para reducir desperdicios\n")

def Transparencia_botelle(self):
    print("su material permite observar el nivel y color del líquido dentro\n")

# Código principal
botellap = BotellaPlastica("plástico", 500, "cilíndrica", "moderno", "roscada", "geométricos")
botellap.imprimir_datos()
print(botellap.contener_liquidos())
print(botellap.facilitar_el_vertido())
print(botellap.cierre_hermetico())
print(botellap.transporte())
print(botellap.manejo())
print(botellap.compatibilidad_bebidas())
print(botellap.reutilizacion())
print(botellap.transparencia())




