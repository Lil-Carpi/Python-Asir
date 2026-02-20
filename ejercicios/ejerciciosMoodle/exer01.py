'''
Crea una llista de valors numèrics enters, no fa falta llegir-la del teclat.
Mitjançant un bucle crea una segona llista, igual a l’anterior, però modificant tots els valors negatius per el seu valor en positiu. Mostra les dues llistes per consola.
Exemple:
Llista 1: [45, -6, 0, -32, 23, 9]
Resultat:
Llista 1: [45, -6, 0, -32, 23, 9]
Llista 2: [45, 6, 0, 32, 23, 9]
'''


def llistas():

    """
        Pasa valores de una lista ya definidos a positivo. Si está en positivo, quedan igual.

        lista1: Se define la lista con valores mixtos.

        Bucle for selecciona los numeros de la lista, y si estos son negativos, se le hace la resta
        para pasar a positivo. Despues, se añaden los numeros ahora positivo a la segunda lista.

        Por último, se imprimen ambas listas.
    """
    llista1 = [45, -6, 0, -32, 23, 9]

    llista2 = []

    for i in llista1:
        if i < 0:            
            i = -i
        llista2.append(i)

    print(f"Llista 1: {llista1}")
    print(f"Llista 2: {llista2}")

llistas()