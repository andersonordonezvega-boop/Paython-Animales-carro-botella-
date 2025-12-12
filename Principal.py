from carroAnderson import Carro 
from deportivo import Deportivo
from Camioneta import CamionetaBlanca
from Dobletroque import DobleTroque

# --- CÓDIGO PRINCIPAL ---
BMW_M2 = Deportivo("BMW M2", "Azul", "3.0 L V6", 2, 2, "Gasolina")
BMW_M2.imprimir_datos()
BMW_M2.arranque()
BMW_M2.apagado()
BMW_M2.aceleracion()
BMW_M2.frenado()
BMW_M2.direccional()
BMW_M2.luces()
BMW_M2.climatizacion()
BMW_M2.tipo_de_seguridad()
BMW_M2.sistemas_de_espejos()
BMW_M2.sistemas_de_ventanas()
print("\n")


camioneta = CamionetaBlanca("Ford Transit", "Negro", "1.5 L V6", 4, 3, "Gasolina")
camioneta.imprimir_datos()
camioneta.arranque()
camioneta.apagado()
camioneta.aceleracion()
camioneta.frenado()
camioneta.direccional()
camioneta.luces()
camioneta.climatizacion()
camioneta.tipo_de_seguridad()
camioneta.sistemas_de_espejos()
camioneta.sistemas_de_ventanas()
print("\n")

bolqueta = DobleTroque("Volvo Trucks", "Amarillo", "D8.8 L", 2, 2, "Diésel")
bolqueta.imprimir_datos()
bolqueta.arranque()
bolqueta.apagado()
bolqueta.aceleracion()
bolqueta.frenado()
bolqueta.direccional()
bolqueta.luces()
bolqueta.climatizacion()
bolqueta.tipo_de_seguridad()
bolqueta.sistemas_de_espejos()
