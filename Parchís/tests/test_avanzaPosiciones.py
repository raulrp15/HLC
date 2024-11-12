from Parchis.Parchis import *

parchis = Parchis('Pablo', 'Raul')

def test_avanzaPosiciones1():
    parchis.dado1 = 1
    parchis.dado2 = 1
    parchis.avanzaPosiciones(1)
    assert parchis.fichaJ1 == 2

def test_avanzaPosiciones2():
    parchis.dado1 = 1
    parchis.dado2 = 1
    parchis.avanzaPosiciones(2)
    assert parchis.fichaJ2 == 2

def test_avanzaPosiciones3():
    parchis.dado1 = 1
    parchis.dado2 = 1
    parchis.fichaJ1 = 19
    parchis.avanzaPosiciones(1)
    assert parchis.fichaJ1 == 19

def test_avanzaPosiciones4():
    parchis.dado1 = 1
    parchis.dado2 = 6
    parchis.fichaJ2 = 15
    parchis.avanzaPosiciones(2)
    assert parchis.fichaJ2 == 18

def test_avanzaPosiciones5():
    parchis.dado1 = 1
    parchis.dado2 = 6
    parchis.fichaJ2 = 12
    parchis.avanzaPosiciones(2)
    assert parchis.fichaJ2 == 19