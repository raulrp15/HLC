from functions.Ahorcado import Ahorcado

def test_generaPalabras1():
    ahorcado = Ahorcado()
    ahorcado.generaPalabras()
    assert ahorcado.palabras.__contains__(ahorcado.palabraSecreta)
