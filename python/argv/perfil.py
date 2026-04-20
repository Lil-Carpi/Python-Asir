import sys

def perfilcreator(nombre, edad):
    return f"Perfil creado: {nombre}, edad {edad} años."


def main():
    args = sys.argv[1:]

    nombre = None
    edad = None

    argval = 0

    while argval < len(args):
        arg = args[argval]

        if arg in ("-h", "--help"):
            print("\n Ayuda")
            print(" -n , --nombre   : Especifica el nombre del usuario")
            print(" -e , --edad     : Especifica la edad del usuario")
            return
        
        elif arg in ("-n", "--nombre"):
            if argval + 1 < len(args):
                nombre = str(args[argval + 1])
                argval += 1
            else:
                print("Error: Falta especificar el nombre del usuario")

        elif arg in ("-e", "--edad"):
            if argval + 1 < len(args):
                edad = str(args[argval + 1])
                argval += 1
            else:
                print("Error: Falta especificar la edad del usuario")


        else:
            print(f"Aviso: Se ha ignorado el argumento desconocido '{arg}'")

        argval += 1


    if nombre and edad:  
        bombo = perfilcreator(nombre, edad)
        print(bombo)
    elif nombre or edad:
        print("Faltan parametros, o nombre o edad.")
    else:
        print("No has introducido ningun parametro. Usa -h para ver la ayuda.")





if __name__ == "__main__":
    main()