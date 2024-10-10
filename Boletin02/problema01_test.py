from Problema01 import *

def test_cifCesar():
    assert cifCesar(2,"a") == "c"

def test_cifCesar2():
    assert cifCesar(3, "a") == "d"

def test_cifCesar3():
    assert cifCesar(7, "a") == "h"

def test_cifCesar4():
    assert cifCesar(2, "z") == "b"