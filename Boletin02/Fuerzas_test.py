from Fuerzas import CalculoFuerzas

def test_Fuerzas1():
    assert CalculoFuerzas("D=32", "T=4") == "V=8"

def test_Fuerzas2():
    assert CalculoFuerzas("T=4", "V=8") == "D=32"

def test_Fuerzas3():
    assert CalculoFuerzas("V=8", "D=32") == "T=4"

def test_Fuerzas4():
    assert CalculoFuerzas("D=10", "T=2") == "V=5"