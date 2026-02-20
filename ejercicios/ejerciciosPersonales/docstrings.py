def suma(n1, n2):
    """
        Funcion suma.
        Hace el calculo de suma con las variables que se le indique
        como argumento.

        Args:
                n1 (int) = primer argumento
                n2 (int) = segundo argumento

                Returns:
                Devuelve la suma de los argumentos.
        """
    suma = n1 + n2
    print(f"Resultado: {suma}")


'''
if __name__ == "__main__":
    n1 = int(input("introduce el primer numero: "))
    n2 = int(input("introduce el segundo numero: "))
    suma(n1, n2)
else:
    print("Importado correctamente")
    print("Funciones disponibles:")
    print("- suma()")
    print("Para mas info, ejecute help(funcion)")
'''
print(suma.__doc__)
