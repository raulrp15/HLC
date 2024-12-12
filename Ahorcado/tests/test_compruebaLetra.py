from functions.Ahorcado import Ahorcado

def test_compruebaLetra1():
    ahorcado = Ahorcado()
    ahorcado.palabraSecreta = "humanidad"
    ahorcado.palabraPista = "_________"
    ahorcado.compruebaLetra('a')
    assert ahorcado.palabraPista == "___a___a_"

def test_compruebaLetra2():
    ahorcado = Ahorcado()
    ahorcado.palabraSecreta = "humanidad"
    ahorcado.palabraPista = "_________"
    ahorcado.compruebaLetra('d')
    assert ahorcado.palabraPista == "______d_d"

def test_compruebaLetra3():
    ahorcado = Ahorcado()
    ahorcado.palabraSecreta = "humanidad"
    ahorcado.palabraPista = "_________"
    ahorcado.compruebaLetra("A")
    assert ahorcado.palabraPista == "___a___a_"

def test_compruebaLetra4():
    ahorcado = Ahorcado()
    ahorcado.palabraSecreta = "persona"
    ahorcado.palabraPista = "_______"
    ahorcado.compruebaLetra("r")
    assert ahorcado.palabraPista == "__r____"

def test_compruebaLetra5():
    ahorcado = Ahorcado()
    ahorcado.palabraPista = "___a___a_"
    ahorcado.palabraSecreta = "humanidad"
    ahorcado.compruebaLetra("m")
    assert ahorcado.palabraPista == "__ma___a_"

def test_compruebaLetra6():
    ahorcado = Ahorcado()
    ahorcado.palabraPista = "___a___a_"
    ahorcado.palabraSecreta = "humanidad"
    ahorcado.compruebaLetra("x")
    assert ahorcado.palabraPista == "___a___a_" and ahorcado.noAcertadas == " x"