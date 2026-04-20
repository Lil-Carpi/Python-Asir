'''
|----------------------------------------------------|
| Nom: Sebastian Ariel                               |
| Cognoms: Duarte Oruez                              |
| Data: 12/01/2026                                   |
|----------------------------------------------------|

RA2. Pràctica 1

Agrupa tots els exercicis en un únic fitxer A02.1_Nom_Cogmon.py. 
Posa un comentari a l’inici de cada exercici indicant quin és. 
Els exercicis han de funcionar amb qualsevol conjunt de dades de prova

1- (1p) Crear una funcio menu amb match. (OBLIGATORI fer el menu)
En acabar una opcio cal tornar a mostar el menu.
El menu conté  les següents opcions:
1. Millor Oferta
2. Romans
3. Pacte
4. Correcte
5. Sortir.

per exemple:
.:: MENU ::.
1. Millor Oferta
2. Romans
3. Pacte
4. Correcte
5. Sortir.

Quina opció vols fer? 



2-(2p) Crea una funció millorOferta que a partir d’un diccionari amb ofertes per a la compra de l’illa de Groenlàndia, 
ens retorni quina és la millor o millors.
La funció tindrà un paràmetre que consistirà en un diccionari amb les diverses ofertes,
 la clau serà el nom de qui fa l’oferta i el valor serà el preu que s’ofereix:
Exemple:
{'Trump': 0, 'Musk': 99000000000, 'Catalunya': 99000000000, 'Canadà': 123456789,
'Aràbia Saudí': 98999999999, 'Rússia': 222222222}
La funció retornarà un altre diccionari amb l’oferta més alta, si hi ha empat ha de retornar totes les que siguin iguals a la més alta.
Amb l’exemple anterior, el resultat seria: {'Musk':99000000000,'Catalunya':99000000000}

3-(2p) Els nombres romans es componen dels caràcters I, V, X, L, C, D, M. Crea una funció
romans que ens informi de si un string és un nombre romà o no.
Exemples:
'III' True
'MCMXCIX' True
'78CVX' False
'MCSFT' False

4-(2,5p) Crea una funció amb identificador pacte que retorni cert o fals indicant si un pacte concret pot ser suficient 
per aprovar els pressupostos generals del país dels Barrufets. La funció tindrà dos paràmetres, el primer serà un 
diccionari amb les dades dels diferents grups parlamentaris que formen el pacte, la clau és el nom del grup i el 
valor és la quantitat d’escons. 
El segon paràmetre serà la quantitat necessària per obtenir majoria absoluta.
La funció ha de fer la suma dels escons i retornar True si és més gran o igual a la majoria absoluta, en altre cas ha de retornar False.
Exemples:
El diccionari conté:
{'Per Pebrots': 137, 'Volem Objectius Xupis': 33}
Majoria: 176
Retorna False
El diccionari conté:
{'Preferim Sistemes Operatius Embedded': 121, 'BARRUFAR': 31, 'Esperem Resposta
Concreta': 7, 'Jumanji': 7, 'Eso Ha Barrufado': 6, 'Podríem No Votar': 5}
Majoria: 176
Retorna True

5-(2,5p) Volem fer servir strings amb la característica que siguin una combinació alternada dels caràcters @@ i &. 
Per exemple : '@@&@@&@@&@@&@@' o '&@@&@@'.
Però resulta que ens proporcionen alguns casos defectuosos que no compleixen aquest requisit, per
exemple : '&@&@&@&@&@' o '&@@@@@'.
Necessitem una funció correcte per detectar aquest casos, la funció tindrà un paràmetre amb l’string que volem verificar i 
retornarà un boolean indicant True si l’string és correcte o False si és incorrecte.
Exemples:
'@@&@@&@@&@@&@@' ha de retornar True
'&@@&@@' ha de retornar True
'&@@&@@&@@&@@&' ha de retornar True
'&@@@@@' ha de retornar False
'@@&@&&@@&@@&@@' ha de retornar False
'&@&@&@&@&@' ha de retornar False

'''

def millorOferta():
    print("Executant: millorOferta \n <incomplet>")

    #ofertes = {'Trump': 0, 'Musk': 99000000000, 'Catalunya': 99000000000, 'Canadà': 123456789, 'Aràbia Saudí': 98999999999, 'Rússia': 222222222}
    #millorOferta = []



    #for clave in ofertes:
    #    print(f"clave {clave}, Valor {ofertes[clave]}")
    #    millorOferta.append(clave)

        

    #for clave, valor in ofertes.items():
    #    print(clave, valor)

    #for oferta in ofertes.items():

    #    print(oferta)
    
    
    #print(millorOferta)

    #for oferta in ofertes:
    #print(ofertes)


def romans():
    print("Executant: romans")
    numeros = ["I", "V", "X", "L", "C", "D", "M"]
    numero = input("Introdueix un número romà\n> ")
    comprovacio = False
    if numero in numeros:
        comprovacio = True
        print(f"{numero}: {comprovacio}")
    else:
        print(f"{numero}: {comprovacio}")

def pacte():
    print("Executant: pacte \n <incomplet>")


def correcte():
    print("Executant: correcte \n <incomplet>")


def menu():
    print("====Menu====")
    print("1. Millor oferta")
    print("2. Romans")
    print("3. Pacte")
    print("4. Correcte")
    print("5. Sortir")
    
    try:
        opcio = int(input("Quina opcio vols fer? \n > "))
    except ValueError:
        print("Valor invalid. Torni a intentar-ho.")
        return menu()
    else:
        if opcio > 5 or opcio <= 0:
            print("Opcio fora de rang. Torni a intentar-ho.")
            return menu()

    match opcio:
  
        case 1:
            millorOferta()
            return menu()
        case 2:
            romans()
            return menu()
        case 3:
            pacte()
            return menu()
        case 4:
            correcte()
            return menu()
          
        case 5:
            print("Sortir seleccionat")
            print("Adeu")


menu()