from Parchis.Parchis import *

def test_esGanador1():
    parchis = Parchis('Raul', 'Pablo')
    parchis.fichaJ1 = 20
    assert parchis.esGanador() == "Raul"

def test_esGanador2():
    parchis = Parchis('Raul', 'Pablo')
    parchis.fichaJ2 = 20
    assert parchis.esGanador() == "Pablo"

def test_esGanador3():
    parchis = Parchis('Raul', 'Pablo')
    assert parchis.esGanador() == ""

def test_esGanador4():
    parchis = Parchis('Marco', 'Hector')
    parchis.fichaJ2 = 20
    assert parchis.esGanador() == "Hector"