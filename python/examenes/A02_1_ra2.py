def millorOferta(ofertes):
    if not ofertes:
        return {}

    maxPreu = max(ofertes.values())

    resultat = {nom: preu for nom, preu in ofertes.items() if preu == maxPreu}
    return resultat

def romans(text):
    caractersRomans = {'I', 'V', 'X', 'L','C','D', 'M'}
    for lletra in text:
        if lletra not in caractersRomans:
            return False
    return True

def pacte(grups, majoria):
    totalEscons = sum(grups.values())
    return totalEscons >= majoria

def correcte(cadena):
    #if "@@@" in cadena or "&&" in cadena or "@&" in cadena.replace("@@", "X") and "X" not in cadena.replace("@@", "X"):
    temp = cadena.replace("@@","X")
    if "@" in temp: return False
    if "XX" in temp or "&&" in temp: return False
    return True
    

def menu():
    print(".:: MENU ::.")
    print("1. Millor oferta")
    print("2. Romans")
    print("3. Pacte")
    print("4. Correcte")
    print("5. Sortir")
    
    try:
        seleccio = int(input("Seleccioni una de les opcions \n > "))
    except ValueError:
        print("Valor invalid. Torni a intentar-ho")
        return menu()
    else:
        if seleccio > 5 or seleccio <= 0:
            print("Opcio fora de rang. Torni a intentar-ho")
            return menu()

    match seleccio:
        case 1:
            dades={'Trump': 0, 'Musk': 99000000000, 'Catalunya': 99000000000, 'Canadà': 123456789, 'Aràbia Saudí': 98999999999, 'Rússia': 222222222}
            print(f"Millor oferta {millorOferta(dades)}")
            return menu()
        case 2:
            test = input("Escriu un numero romà: ")
            print(f"És romà? {romans(test.upper())}")
            return menu()
        case 3:
            pacteTest = {'Preferim Sistemes Operatius Embedded': 121, 'BARRUFAR': 31, 'Esperem Resposta Concreta': 7, 'Jumanji': 7, 'Eso Ha Barrufado': 6, 'Podríem No Votar': 5}
            majoria = 176
            print(f"S'aprova el pacte? {pacte(pacteTest, majoria)}")
            return menu()
        case 4:
            cadenaTest = input("Introdueix la cadena (ex: @@&@@&@@): ")
            print(f"És correcta? {correcte(cadenaTest)}")
            return menu()
        case 5:
            print("Adeu")


if __name__ == "__main__":
    menu()

