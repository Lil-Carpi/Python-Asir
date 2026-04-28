"""
Fitxers de text

1- Crea un mètode mostra, que a partir d'un nom de fitxer, mostri el seu contingut per consola. Si el fitxer no és vàlid, ha de mostrar un missatge informatiu.

2- Crea un mètode concatena, que a partir de dos fitxers, afegeixi el contingut del segon fitxer al primer fitxer. 
Si el segon fitxer no és vàlid, ha de mostrar un missatge informatiu.

3- Crea un mètode afegir, que escrigui el contingut d'una llista en un fitxer. S'ha de fer append, el contingut original del fitxer no s'ha d'esborrar.

4- Crea un mètode escriuPos, que escrigui una frase en un fitxer, a una posició concreta. Si la posició és incorrecta, ha de mostrar un missatge informatiu.
"""
import sys
from pathlib import Path

def usage():
    # La ayuda.
    print("Ayuda")
    print(" -c, --cat           : Muestra el contenido de un fichero a partir de su nombre")
    print(" -c2f, --concat2file : Concatena el contenido del el segundo fichero pasado al primero.")
    print(" -l, --listar        : Escribe el contenido de una lista en un fichero, sin alterar el contenido original.")
    print(" -e, --echoPos       : Escribe en la linea que indiques")

def mostra(filename): # Hecho
    print(f"Valor pasado: {filename} \nMostrar contenido del fichero")
    try:
        with open(filename) as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: El fichero {filename} no existe."
    
    # Intenta
        # abre el fichero pasado como file, cierralo despues
            # devuelve el contenido del fichero pasado.
    # Si da el error del tipo FileNotFoundError:
        # Devuelve que el fichero pasado no existe.


def concatena(Ffile, Sfile): # Hecho
    print(f"Valor pasado: {Ffile}, {Sfile} \n añade el contenido de {Sfile} a {Ffile}")
    segundo = Path(Sfile)
    if segundo.exists():
            with open(Ffile, "a") as first,  open(Sfile) as second:
                first.write(second.read())
                return "Hecho. Verifica el fichero para ver los cambios."
    else:
        print(f"El archivo {Sfile} no existe")
        

    # guarda el path del segundo fichero
    # si el segundo fichero existe:
        # abre el primer fichero pasado para concatenar como first, y abre tambien el segundo fichero para leer como segundo:
            # escribe el contenido del segundo fichero en el primer fichero.
            # Devuelve un mensaje de que se ha escrito con exito.
    # Si no:
        # Imprime que el segundo fichero no existe.


def afegir(filename, llista):
    print(f"Valor pasado: {llista}\nescribe el contenido de una lista en un fichero (con append) y el contenido original no se ha de borrar")

def escriuPos(filename, frase, linea):
    print(f"Valor pasado:{frase}, {linea}\n Escribe una frase en la posicion concreta que se le pase.")


def main():
    print("main")

    args = sys.argv[1:] # Almacena los parametros pasadas
    # Dame todos los elementos de la lista descartando el nombre del fichero.

    argval = 0 # valor de variable
    #Puntero. Para recordar en que posicion de la lista args se esta leyendo.

    ##### NOTA AL SUMAR ARGVAL ####
    # Se suma la cantidad de acciones que se realiza en ese parametro,
    # Por ejemplo, en c2f, se pasa el argumento c2f (1) y los dos ficheros (1 + 2). Son 3 argumentos en total.
    # Esto ayuda a saber cuando parar el bucle while.
    
    if args == []: # Si no se pasa ningun parametro
        usage()    # Se devuelve el help

    while argval < len(args):
    ## Bucle while
    # Mientras la posicion actual de mi puntero sea MENOR a la longitud que la cantidad de argumentos
    # que tengo, sigue rulando.

    ## Explicacion mas sencilla del bucle while:
    # Si las sumas que hacemos en cada parametro (cuando se pone el argval += 2, por ejemplo, de la linea 88) no superan
    # la cantidad de variables que se pasa (lo que se cuenta en args), sigue rulando.
    
        arg = args[argval]
        # Se pilla el texto en la posicion actual del puntero
        # y se pone en arg para mas comodidad.
        # Por ejemplo: arg podria valer "-c". Esto facilita pasar entre las evaluaciones de comandos.


        if arg in ("-h", "--help"):
            usage()
            return
            # Si arg vale "-h" o "--help"
            # Devuelve la ayuda y sal.
        
        elif arg in ("-c","--cat"):
            if argval + 1 < len(args):
                filename = str(args[argval + 1])
                print(mostra(filename))
                argval += 2
            else:
                print("Error: Falta especificar el nombre del fichero. Usa '-h' o '--help' para ver la ayuda.")
                argval +=1

            # Si arg vale "-c" o "--cat", ejecuta
            # Si existe al menos un elemento mas despues del -c (que deberia ser el nombre del fichero), ejecuta
                # Guarda en la variable filename, el string del elemento que viene despues de -c.
                # Imprime el return de la funcion mostra pasandole la variable filename.
                # Añade 2 puntos al puntero. Asi el while volvera a leer pero saltará esta parte.
            # Si no:
                # Imprime que falta especificar el nombre del fichero
                # Añade solo 1 punto al puntero. Asi el while volvera a leer pero se saltará esta parte (Solo si el usuario pone un "-c" y nada mas, salta al siguiente).

        elif arg in ("-c2f","--concat2file"):
            if argval + 2 < len(args):
                Ffile = str(args[argval + 1])
                Sfile = str(args[argval + 2])
                resultado = concatena(Ffile, Sfile)
                print(resultado)
                argval += 3
            else:
                print("Error: Falta especificar los ficheros a concatenar. Usa '-h' o '--help' para ver la ayuda.")
                argval +=1

            # Si arg vale "-c2f" o "--concat2file", ejecuta
                # Si existen al menos dos archivos despues del "-c2f" (que deberian ser los dos ficheros), ejecuta
                    # Guarda el primer fichero pasado como string.
                    # Guarda el segundo fichero pasado como sring.
                    # Guarda el resultado en la variable resultado, el cual es el return de la funcion concatena al cual se le ha pasado el primer y segundo fichero consecutivamente.
                    # Imprime la variable resultado.
                    # Añade 3 puntos al puntero.
                # Si no:
                    # Imprime que valta especificar los dos ficheros a concatenar.
                    # Sumale 1 punto al puntero.

        else:
            print(f"Valor {args} no existe.")
            usage()
            return
        ## Si se pasa un parametro que no existe:
            # Pasale el help y sal.
            

if __name__ == "__main__":
    main()