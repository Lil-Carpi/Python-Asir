import sys
import os

'''
|----------------------------------------------------|
| Nom: Sebastian Ariel                               |
| Cognoms: Duarte Oruez                              |
| Data:                                              |
|----------------------------------------------------|

RA2. Pràctica 3

Agrupa tots els exercicis en un únic fitxer A02.3_Nom_Cogmon.py. 
Els exercicis han de funcionar amb qualsevol conjunt de dades de prova

1-(2,5p) Crea un script practica3.py que admeti els següents paràmetres:
-p o --path necessita un paràmetre string
-i o --inicial necessita un paràmetre string
-l o --limit necessita un paràmetre int
--igual
--noigual
--help o -h
Ha de detectar correctament les opcions i paràmetres i mostrar-ne un missatge si n’hi ha cap
dada errònia.
Hi haurà també les següents funcions (aquestes funcions no fan res de moment):
def compta(path):
return 0, 0
def trobaPerInicial(path, inicial):
return []
def trobaNoInicial(path, inicial, limit):
return []
Per cada cas, ha de fer la crida a la funció corresponent:
--igual crida a la funció trobaPerInicial(path, inicial)
--noigual crida a la funció trobaNoInicial(path, inicial, limit)
--help o -h ha de mostrar un missatge informatiu dels paràmetres vàlids.
Si hi ha varis paràmetres, els ha de gestionar tots.
S’ha de fer print dels resultats retornats per les funcions.

2-(2,5p) Crea la funció compta(path). Aquesta funció ha de retornar la quantitat de fitxers i
directoris que hi ha en un path.
Exemple:
qfitxers, qdirec = compta("/home/user/proves")

3-(2,5p) Crea la funció trobaPerInicial(path, lletra). Aquesta funció ha de retornar una llista amb
tots els elements del path que tinguin un nom que comenci per la lletra indicada.
Exemple:
llista = trobaPerInicial("/home/user/proves", "X")
print(llista)
['Xarxa.txt', 'Xemeneia.txt', 'Xocolata.ods']

4-(2,5p) Crea la funció trobaNoInicial(path, lletra, limit). Aquesta funció ha de retornar una llista
amb els elements del path que tinguin un nom que NO comenci per la lletra indicada, però sense
superar la quantitat que indiqui el paràmere limit.
Exemple:
llista = trobaPerInicial("/home/user/proves", "X", 4)
print(llista)
['Backups.txt', 'Bases-de-dades.cnf', 'configs.conf', 'www.sites.d']

Entrega:
A02.3_Nom_Cogmon.py


'''
def compta(path):
    list = 0
    print(f"Llistant {path}")
    try:
        actualPath = os.listdir(path)
        if os.path.exists(path):
            for path in actualPath:
                list = list + 1
            print(list)
    except FileNotFoundError:
        print("La ruta no existeix.")        

def trobaPerInicial(path, inicial):
    list = 0
    #try:
    #    actualPath = os.listdir(path)
    #    if os.path.exists(path):
    #        for inicial in actualPath:
    #            inicial = actualPath[1:]
               
    #except FileNotFoundError:
    #    print("La ruta no existeix.")   
    
    dir = os.listdir(path)  
    #inicial[:]
    print(f"Llistant {path}, amb inicial {inicial}")

    
    return []

def trobaNoInicial(path, inicial, limit):
    print(path, inicial, limit)
    llista = []
    
    #if not path or not inicial:
    #    return llista
    
    #for i in os.listdir(path):
    #    if len(llista) >= limit:
    #        return 1
    #    if not i.startswith

def main():
    args = sys.argv[1:]
    
    argval = 0
    
    while argval < len(args):
        
        if args[argval] in ("-p","--path"):
            if argval + 1 < len(args):
                path=str(args[argval + 1])
                compta(path)
                return
            else:
                print("Error: Requereix una ruta absoluta.")
                
            argval =+ 1
            
            
        elif args [argval] in ("-i","--inicial"):
            if argval + 1 < len(args):
                path=str(args[argval + 1])
                inicial=str(args[argval + 2])
                trobaPerInicial(path, inicial)
                print("inicial")
                return
            else:
                print("Error: Requereix la ruta i la lletra inicial")
            argval =+ 1
        elif args [argval] in ("-l", "--limit"):
            if argval + 1 < len(args):
                limit=int(args[argval + 1])
                trobaNoInicial(limit)
                print("init")
                return
            
            argval =+ 1
        elif args [argval] in ("--igual"):
            if argval + 1 < len(args):
                path=str(args[argval + 1])
                inicial=str(args[argval + 2])
                trobaPerInicial(path, inicial)
                print("igual")
                return
            argval =+ 1
        elif args [argval] in ("--noigual"):
            if argval + 1 < len(args):
                path=str(args[argval + 1])
                inicial=str(args[argval + 2])
                limit=int(args[argval + 3])
                trobaNoInicial(path, inicial, limit)
                print("noigual")
                return
            argval =+ 1
        elif args [argval] in ("-h", "--help"):
            print("\n   .:: Ajuda ::.")
            print("     -h, --help   : Mostra aquesta ajuda.")
            print("     -p, --path   : Compta la quantitat de fitxers o directoris en la ruta que indiqueu.")
            print("     -i, --inicial: Busca el fitxer o directori amb la lletra inicial que indiqueu ")
            print("     --limit      : Busca en la ruta que indiqueu amb l'inicial que indiqueu.")
            print("     --noigual    : Busca la ruta que indiqueu i dona resultat de fitxers o directoris amb l'inicial que indiqueu amb el maxim de caracters que indiqueu.")

            argval =+ 1
if __name__ == "__main__":
    main()
