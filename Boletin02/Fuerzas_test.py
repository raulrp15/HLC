from Fuerzas import CalculoFuerzas

def test_Fuerzas1():
    assert CalculoFuerzas("D=32", "T=4") == "V=8"

def test_Fuerzas2():
    assert CalculoFuerzas("T=4", "V=8") == "D=32"

def test_Fuerzas3():
    assert CalculoFuerzas("V=8", "D=32") == "T=4"

def test_Fuerzas4():
    assert CalculoFuerzas("D=10", "T=2") == "V=5"

def test_Fuerzas5():
    assert CalculoFuerzas("D=32", "T=0") == "No se puede dividir entre 0"

def test_Fuerzas6():
    assert CalculoFuerzas("D=32", "V=8") == "T=4"

def test_Fuerzas7():
    assert CalculoFuerzas("D=0", "V=4") == "T=0"

def test_Fuerzas8():
    assert CalculoFuerzas("V=0", "D=2") == "No se puede dividir entre 0"