"""
Fitxers de text

1- Crea un mètode mostra, que a partir d'un nom de fitxer, mostri el seu contingut per consola. Si el fitxer no és vàlid, ha de mostrar un missatge informatiu.

2- Crea un mètode concatena, que a partir de dos fitxers, afegeixi el contingut del segon fitxer al primer fitxer. 
Si el segon fitxer no és vàlid, ha de mostrar un missatge informatiu.

3- Crea un mètode afegir, que escrigui el contingut d'una llista en un fitxer. S'ha de fer append, el contingut original del fitxer no s'ha d'esborrar.

4- Crea un mètode escriuPos, que escrigui una frase en un fitxer, a una posició concreta. Si la posició és incorrecta, ha de mostrar un missatge informatiu.
"""
import sys

def mostra(filename):
    print(f"Valor pasado: {filename} \nMostrar contenido del fichero")
    try:
        with open(filename) as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: El fichero {filename} no existe."


def concatena(Ffile, Sfile):
    print(f"Valor pasado: {Ffile}, {Sfile} \n añade el contenido de {Sfile} a {Ffile}")
    try:
        second = open(Sfile)
        second.close()
        with open(Ffile, a) as first:
            Ffile.write(second)
            
            


def afegir(llista):
    print(f"Valor pasado: {llista}\nescribe el contenido de una lista en un fichero (con append) y el contenido original no se ha de borrar")

def escriuPos(frase, linea):
    print(f"Valor pasado:{frase}, {linea}\n Escribe una frase en la posicion concreta que se le pase.")


def main():
    print("main")
    # Valores a pasar
    filename=None
    Ffile = None
    Sfile = None
    llista = None
    frase = None
    linea = None

    # Activacion de variables
    cat = False
    concat2file = False
    listar = False
    echoPos = False

    args = sys.argv[1:]
    argval = 0

    while argval < len(args):
        arg = args[argval]

        if arg in ("-h", "--help"):
            print("\n Ayuda")
            print(" -c, --cat           : Muestra el contenido de un fichero a partir de su nombre")
            print(" -c2f, --concat2file : Concatena el contenido del el segundo fichero pasado al primero.")
            print(" -l, --listar        : Escribe el contenido de una lista en un fichero, sin alterar el contenido original.")
            print(" -e, --echoPos       : Escribe en la linea que indiques")
            return
        
        elif arg in ("-c","--cat"):
            if argval +1 < len(args):
                filename = str(args[argval + 1])
                argval += 1
            else:
                print("Error: Falta especificar el nombre del fichero.")

        argval += 1

        if filename:
            result = mostra(filename)
            print(result)


if __name__ == "__main__":
    main()