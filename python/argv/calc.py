import sys

def sumador(d1, d2):
    return d1 + d2
    

def restador(d1, d2):
    return d1 - d2

def main():
    args = sys.argv[1:]
    d1 = None
    d2 = None
    suma = None
    resta = None
    argval=0
    while argval < len(args):
        arg = args[argval]

        if arg in ("-h", "--help"):
            print("\n Ayuda")
            print("-a       : Indica el primer parametro a calcular")
            print("-b       : Indica el segundo parametro a calcular")
            print("--suma   : Indica al programa que sume los dos valores")
            print("--resta  : Indica al programa que reste los dos valores")
            return
        elif arg in ("-a"):
            if argval + 1 <len(args):
                d1 = int(args[argval + 1])
                argval += 1
            else:
                print("Error: Falta especificar el valor a -a")
        elif arg in ("-b"):
            if argval +1 < len(args):
                d2 = int(args[argval + 1])
                argval += 1
            else:
                print("Error: Falta especificar el valor a -b")
        elif arg == "--suma":
            suma = True
        elif arg == "--resta":
            resta = True
        else:
            print(f"Aviso: se ha ignorado el argumento desconocido '{arg}'")
        argval += 1
    
    if suma and resta:
        print("Solo puedes hacer una operacion a la vez.")
    
    if not suma and not resta:
        print("Error: Debes indicar una operacion. Usa -h para ver la ayuda.")
        return

    if d1 is None or d2 is None:
        print("Error: Faltan numeros para realizar la operacion.")
        return
    if suma:
        resultado = sumador(d1, d2)
        print(f"El resultado de la suma es {resultado}")
    if resta:
        resultado = restador(d1, d2)
        print(f"El resultado de la resta es {resultado}")
if __name__ == "__main__":
    main()