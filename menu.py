from funciones import *


menu_activo = True
opcion_seleccionada=0
while menu_activo:
    print("Ingrese una de las siguientes opciones")
    print("1.- Calcular IVA")
    print("2.- Descuento de producto")
    print("3.- Calcular IMC")
    print("4.- Salir")
    opcion_seleccionada=int(input("Escriba una opcion: "))


    if opcion_seleccionada == 1:
        print("Selecciono la opción: ", opcion_seleccionada)
        print(calcular_iva(1000))       
    if opcion_seleccionada == 2:
        print("Seleccionó la opción: ",opcion_seleccionada)
        print(descuento_producto(20000,40))
    if opcion_seleccionada == 3:
        print("Seleccionó la opcion: ",opcion_seleccionada)
        print(calcular_IMC(753,1.69))
    if opcion_seleccionada == 4:
        print("")
        menu_activo=False

