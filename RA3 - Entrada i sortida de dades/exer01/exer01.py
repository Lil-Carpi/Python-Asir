"""
Fitxers de text

1- Crea un mètode mostra, que a partir d'un nom de fitxer, mostri el seu contingut per consola. Si el fitxer no és vàlid, ha de mostrar un missatge informatiu.

2- Crea un mètode concatena, que a partir de dos fitxers, afegeixi el contingut del segon fitxer al primer fitxer. 
Si el segon fitxer no és vàlid, ha de mostrar un missatge informatiu.

3- Crea un mètode afegir, que escrigui el contingut d'una llista en un fitxer. S'ha de fer append, el contingut original del fitxer no s'ha d'esborrar.

4- Crea un mètode escriuPos, que escrigui una frase en un fitxer, a una posició concreta. Si la posició és incorrecta, ha de mostrar un missatge informatiu.
"""
import os
import sys


def main():
    args = sys.argv[1:]
    argval = 0

    while argval < len(args):
        if args[argval] == "--h" or "--help":
            if argval +1 < len(args):
                print("hola")
                return
        
        if args[argval] == "-m " or "--mostra":
            if argval +1 < len(args):
                print("si")
                argval =+1



if __name__ == "__main__":
    main()