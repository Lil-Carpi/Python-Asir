def cubito():
    base = int(input("Introduce la base: "))
    altura = int(input("Introduce la altura: "))

    cabeza = "*" * base
    # Al poder multiplicar strings para que salga una y otra vez,
    # se puede hacer tanto la base como la altura.
    cuerpo = "*" + ' ' * (base-2) + "*" + '\n'
    # El cuerpo se puede hacer multiplicando la cantidad
    # de la base menos dos para cuadrar en los costados.
    constructor = cabeza + '\n' + (cuerpo * altura) + cabeza
    # Se unifica todo en una sola variable
    print(constructor)
    # Se imprime el cubito


cubito()
