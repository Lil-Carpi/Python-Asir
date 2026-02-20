print(".::Menu::.")
print("1. Hace algo")
print("2. Salir")

menuStatus = True
while menuStatus == True:
    menuSeleccion = int(input("Introduce una opcion \n >  "))
    match menuSeleccion:
        case 1:
            print("Ejecutando algo")
        case 2:
            print("Adios")
            menuStatus = False
