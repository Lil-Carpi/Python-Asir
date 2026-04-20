import sys
import os

'''
|----------------------------------------------------|
| Nom: Sebastian Ariel                               |
| Cognoms: Duarte Oruez                              |
| Data:                                              |
|----------------------------------------------------|
RA2. Pràctica 3
'''

def compta(path):
    qfitxers = 0
    qdirec = 0
    try:
        # Llistem tot el que hi ha dins la ruta
        for element in os.listdir(path):
            ruta_completa = os.path.join(path, element)
            # Comprovem si és fitxer o directori
            if os.path.isfile(ruta_completa):
                qfitxers += 1
            elif os.path.isdir(ruta_completa):
                qdirec += 1
        return qfitxers, qdirec
    except FileNotFoundError:
        print(f"Error: La ruta '{path}' no existeix.")
        return 0, 0

def trobaPerInicial(path, inicial):
    llista_resultat = []
    try:
        for element in os.listdir(path):
            # Comprovem si comença per la lletra
            if element.startswith(inicial):
                llista_resultat.append(element)
        return llista_resultat
    except FileNotFoundError:
        print(f"Error: La ruta '{path}' no existeix.")
        return []

def trobaNoInicial(path, inicial, limit):
    llista_resultat = []
    try:
        for element in os.listdir(path):
            # Comprovem si NO comença per la lletra
            if not element.startswith(inicial):
                llista_resultat.append(element)
                # Parem si arribem al límit
                if len(llista_resultat) >= limit:
                    break
        return llista_resultat
    except FileNotFoundError:
        print(f"Error: La ruta '{path}' no existeix.")
        return []

def main():
    args = sys.argv[1:]
    
    # Variables per guardar les dades introduïdes
    path = None
    inicial = None
    limit = None
    
    # Variables per saber quina acció s'ha demanat
    fer_igual = False
    fer_noigual = False

    argval = 0
    # 1. Fase de LECTURA de paràmetres
    while argval < len(args):
        arg = args[argval]
        
        if arg in ("-h", "--help"):
            print("\n .:: Ajuda ::.")
            print(" -p, --path <ruta>    : Especifica la ruta a avaluar.")
            print(" -i, --inicial <llet> : Lletra inicial a buscar.")
            print(" -l, --limit <num>    : Límit màxim de fitxers a retornar.")
            print(" --igual              : Executa la cerca de fitxers per inicial.")
            print(" --noigual            : Executa la cerca de fitxers que NO comencin per la inicial.")
            return # Sortim de l'script després de mostrar l'ajuda
            
        elif arg in ("-p", "--path"):
            if argval + 1 < len(args):
                path = str(args[argval + 1])
                argval += 1
            else:
                print("Error: Falta especificar el valor per --path.")
                
        elif arg in ("-i", "--inicial"):
            if argval + 1 < len(args):
                inicial = str(args[argval + 1])
                argval += 1
            else:
                print("Error: Falta especificar el valor per --inicial.")
                
        elif arg in ("-l", "--limit"):
            if argval + 1 < len(args):
                try:
                    limit = int(args[argval + 1])
                except ValueError:
                    print("Error: El límit ha de ser un número enter.")
                argval += 1
            else:
                print("Error: Falta especificar el valor per --limit.")
                
        elif arg == "--igual":
            fer_igual = True
            
        elif arg == "--noigual":
            fer_noigual = True
            
        else:
            print(f"Avís: S'ha ignorat l'argument desconegut '{arg}'")
            
        argval += 1 # Aquesta és la sintaxi correcta per sumar 1

    # 2. Fase d'EXECUCIÓ de les funcions
    
    # L'enunciat no demana un paràmetre específic per `compta`, 
    # però demana retornar i imprimir la quantitat. Ho farem si hi ha un path indicat.
    if path:
        qfitxers, qdirec = compta(path)
        print(f"Al path indicat hi ha {qfitxers} fitxers i {qdirec} directoris.")

    if fer_igual:
        if path and inicial:
            llista = trobaPerInicial(path, inicial)
            print(f"Resultat d'elements que comencen per '{inicial}':")
            print(llista)
        else:
            print("Error: Falta passar els paràmetres --path i --inicial per fer l'acció --igual.")

    if fer_noigual:
        if path and inicial and limit is not None:
            llista = trobaNoInicial(path, inicial, limit)
            print(f"Resultat d'elements que NO comencen per '{inicial}' (límit {limit}):")
            print(llista)
        else:
            print("Error: Falta passar --path, --inicial o --limit per fer l'acció --noigual.")

if __name__ == "__main__":
    main()
