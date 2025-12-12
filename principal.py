from BotellaAnderson import Botellapadre
from base_datos import base_datos


























































# ==== MENÚ ====
bd = base_datos()

while True:
    print("\n=== MENÚ BOTELLAS ===")
    print("1.Agregar  2.Agregar varias  3.Insertar")
    print("4.Eliminar  5.Eliminar pos  6.Buscar")
    print("7.Contar  8.Ordenar  9.Invertir  0.Salir")

    opinion = input("Opción:")

    if opinion == "1":
        bd.agregar_elemento(input("Nombre:"))
    elif opinion == "2":
        bd.agregar_elementos_otra_lista(input("Botellas separadas por coma:").split(","))
    elif opinion == "3":
        bd.insertar_elemento_posicion_especifica(int(input("Posición:")), input("Nombre:"))
    elif opinion == "4":
        bd.eliminar_primer_elemento(input("Nombre:"))
    elif opinion == "5":
        bd.eliminar_elemento_posicion_especificada_y_devuelve(int(input("Posición: ")))
    elif opinion == "6":
        bd.buscar_posicion(input("Nombre:"))
    elif opinion == "7":
        bd.contar_botella(input("Nombre:"))
    elif opinion == "8":
        bd.ordenar_botellas()
    elif opinion == "9":
        bd.invertir_orden_de_los_elementos()
    elif opinion == "0":
        print("Adiós")
        break
    else:
        print("Opción no válida.")