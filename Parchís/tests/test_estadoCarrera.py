from Parchis.Parchis import *

def test_estadoCarrera1():
    parchis = Parchis('Raul', 'Pablo')
    parchis.fichaJ1 = 19
    assert parchis.estadoCarrera() == 'Raul'

def test_estadoCarrera2():
    parchis = Parchis('Raul', 'Pablo')
    parchis.fichaJ2 = 19
    assert parchis.estadoCarrera() == 'Pablo'

def test_estadoCarrera3():
    parchis = Parchis('Raul', 'Pablo')
    assert parchis.estadoCarrera() == 'Empate'

def test_estadoCarrera4():
    parchis = Parchis('Marco', 'Hector')
    parchis.fichaJ2 = 19
    assert parchis.estadoCarrera() == 'Hector'

def test_estadoCarrera5():
    parchis = Parchis('Marco', 'Hector')
    parchis.fichaJ1 = 19
    assert parchis.estadoCarrera() == 'Marco'

def test_estadoCarrera6():
    parchis = Parchis('Marco', 'Hector')
    parchis.fichaJ1 = 19
    parchis.fichaJ2 = 19
    assert parchis.estadoCarrera() == 'Empate'