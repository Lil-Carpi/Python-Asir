import os
import sys


def llista(num):
    try:
        num = int(num)
        if num < 1:
            print("El número ha de ser >= 1")
            return
    except ValueError:
        print("Error: El paràmetre per a --lista ha de ser un número enter.")
        return

    try:
        elements = os.listdir('.')
        if not elements:
            print("DIRECTORY BUIT")
        else:
            for element in elements[:num]:
                print(element)

    except Exception as e:
        print(f"Error en llegir el directori: {e}")


def snom(nom):
    if not os.path.exist(nom):
        print("NO EXISTEIX")
    elif os.path.isdir(nom):
        print("DIRECTORI")
    elif os.path.isfile(nom):
        print("FITXER")


def ajuda(funcio=None, completa=True):
    if completa:
        print("\n.:: AJUDA GENERAL ::.")
        print(f"Ús del script: python3 {sys.argv[0]} [opcions]")
        print("Opcions disponibles:")
        print("  --llista <num> : Mostra els primers <num> elements del directori actual")
        print("  -s <nom>       : Indica si <nom> és un fitxer, un directori o no existeix.")
        print("  -h, --help     : Mostra aquesta ajuda general.")
        print("  -h <funcio>    : Mostra ajuda d'uina funcio ('llista' o 'snom').\n")
    elif funcio == 'snom': 
        print("Funció snom:")
        print("Ús: -s <nom>")
        print("El paràmetre <nom> és la ruta (path) d'un arxiu o directori a comprovar.")
    else:
        print(f"No hi ha ajuda específica per la funció: {funcio}")


def main():
    args = sys.argv[1:]

    if not args:
        ajuda(completa=True)
        return

    i = 0
    while i < len(args):
        arg = args[i]

        if arg == "--lista":
            if i + 1 < len(args) and not args[i+1].startswith('-'):
                llista(args[i+1])
                i += 1
            else:
                print("Error: Falta el paràmetre num per a --lista")

        elif arg == "-s":
            if i +1 < len(args) and not args[i+1].startswith('-'):
                snom(args[i+1])
                i += 1
            else:
                print("Error: Falta el paràmetre nom per a -s")

        elif arg in ('--help', '-h'):
            if i + 1 < len(args) and not args[i+1].startswith('-'):
                funcHelp = args[i+1]
                ajuda(funcio=funcHelp, completa=False)
                i += 1
            else:
                ajuda(completa=True)

        else:
            print(f"Paràmetre ignorat o desconegut: {arg}")

        i += 1



if __name__ == "__main__":
    main()
