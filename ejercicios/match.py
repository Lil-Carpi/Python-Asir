# La idea es intentar hacer un menu el cual se ejecute una y otra vez cada que se termina de hacer una opcion.
# En el ejercicio real se pedira una serie de programas alojados en funciones, que se llamaran cada que se seleccione dentro del match con el valor que pase el usuario.

def bucle():
    program_value = True
    while program_value:
        try:
            option = int(input("Seleccione una de las opciones: ")) 
        except ValueError:
            print("No ha ingresado un valor valido")
            continue

        match option:
            case 1:
                print("xd")
            case 2:
                print("dx")
            case 3:
                print("lx")
            case 4:
                print("chao")
                program_value = False

"""
    program_value=True # El valor del prorgrama es True
    option = int(input("Seleccione una de las opciones: "))

    match option:

        case 1:
            print("cx")
            return 1
            bucle() # Esto se deberia de mirar para ver si es correcto.
                    # La idea es volver a llamar la funcion de nuevo, lo que podria no ser del
                    # todo correcto. 
        case 2:
            print("cxs")
            bucle()
        case 3:
            program_value=False # Cambia el valor de program_value por False
        
    if program_value==False: 
        return 0 # Esto no se si es correcto: ya que devuelve nada y finaliza la funcion.
"""
bucle()
