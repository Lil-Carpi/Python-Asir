# Importamos las funciones de tu archivo (asegúrate de que no haya espacios en el nombre del archivo)
# He supuesto que tu archivo se llama A02.1_ra2.py sin el ".py"
from A02_1_ra2 import millorOferta, romans, pacte, correcte

def test_millorOferta():
    ofertes = {
        'Trump': 0, 'Musk': 99000000000, 'Catalunya': 99000000000, 
        'Canadà': 123456789, 'Aràbia Saudí': 98999999999, 'Rússia': 222222222
    }
    esperat = {'Musk': 99000000000, 'Catalunya': 99000000000}
    
    assert millorOferta(ofertes) == esperat, "Error en millorOferta"
    print("✅ millorOferta superado")

def test_romans():
    assert romans('III') == True, "Falla en 'III'"
    assert romans('MCMXCIX') == True, "Falla en 'MCMXCIX'"
    assert romans('78CVX') == False, "Falla en '78CVX'"
    assert romans('MCSFT') == False, "Falla en 'MCSFT'"
    print("✅ romans superado")

def test_pacte():
    # Caso 1: Falso
    grups1 = {'Per Pebrots': 137, 'Volem Objectius Xupis': 33}
    assert pacte(grups1, 176) == False, "Error en pacte (Caso 1)"
    
    # Caso 2: Verdadero
    grups2 = {
        'Preferim Sistemes Operatius Embedded': 121, 'BARRUFAR': 31, 
        'Esperem Resposta Concreta': 7, 'Jumanji': 7, 
        'Eso Ha Barrufado': 6, 'Podríem No Votar': 5
    }
    assert pacte(grups2, 176) == True, "Error en pacte (Caso 2)"
    print("✅ pacte superado")

def test_correcte():
    # Casos verdaderos
    assert correcte('@@&@@&@@&@@&@@') == True, "Falla en '@@&@@&@@&@@&@@'"
    assert correcte('&@@&@@') == True, "Falla en '&@@&@@'"
    assert correcte('&@@&@@&@@&@@&') == True, "Falla en '&@@&@@&@@&@@&'"
    
    # Casos falsos
    assert correcte('&@@@@@') == False, "Falla en '&@@@@@'"
    assert correcte('@@&@&&@@&@@&@@') == False, "Falla en '@@&@&&@@&@@&@@'"
    assert correcte('&@&@&@&@&@') == False, "Falla en '&@&@&@&@&@'"
    print("✅ correcte superado")

# Ejecutamos todos los tests
if __name__ == "__main__":
    print("Iniciando pruebas...\n" + "-"*20)
    test_millorOferta()
    test_romans()
    test_pacte()
    test_correcte()
    print("-"*20 + "\n🎉 ¡Todos los tests funcionan perfectamente!")
