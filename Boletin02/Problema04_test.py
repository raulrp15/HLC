from Problema04 import *
def test_Kaprekar1():
    assert Kaprekar(6174) == 0

def test_Kaprekar2():
    assert Kaprekar(1111) == 8

def test_Kaprekar3():
    assert Kaprekar(9999) == 8

def test_Kaprekar4():
    assert Kaprekar(1893) == 7

def test_Kaprekar5():
    assert Kaprekar(1121) == 5

def test_Kaprekar6():
    assert Kaprekar(3524) == 3