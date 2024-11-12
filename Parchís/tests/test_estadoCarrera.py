from Parchis.Parchis import *

def test_estadoCarrera1():
    parchis = Parchis('Raul', 'Pablo')
    parchis.fichaJ1 = 19
    assert parchis.estadoCarrera() == 'Raul va ganando'

def test_estadoCarrera2():
    parchis = Parchis('Raul', 'Pablo')
    parchis.fichaJ2 = 19
    assert parchis.estadoCarrera() == 'Pablo va ganando'

def test_estadoCarrera3():
    parchis = Parchis('Raul', 'Pablo')
    assert parchis.estadoCarrera() == 'Empate, nadie va ganando'

def test_estadoCarrera4():
    parchis = Parchis('Marco', 'Hector')
    parchis.fichaJ1 = 19
    parchis.fichaJ2 = 19
    assert parchis.estadoCarrera() == 'Empate, nadie va ganando'