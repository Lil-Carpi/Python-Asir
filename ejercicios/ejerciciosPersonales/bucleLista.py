"""valores = {'primero':1, 'segundo':2, 'tercero':3}


for i in valores:
    print(i)

for i in valores.values():
    print(i)

for i, k in valores.items():
    print(i, k)

for i, k in valores.items():
    print('string =', i, ', numero = ', k)

for i in range(1, 11, 2):
    print(i)

coleccion = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for e in coleccion:
    if e % 2 != 1:
        print(e)
"""
numeros = [1, 2, 3, 4, 5, 6]
for i in numeros:
    if i == 5:
        print(i)
        print("found")
        break
else:
    print("Not found")
