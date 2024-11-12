from Parchis.Parchis import *

objeto = Parchis('Raul', 'Pablo')

def test_pintaTablero1():
    objeto.fichaJ1 = 0
    objeto.fichaJ2 = 0
    esperado = '\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\tF\n'
    esperado += 'Raul\tI\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n'
    esperado += 'Pablo\tI\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF'
    cadena = objeto.pintaTablero()
    assert cadena == esperado


def test_pintaTablero2():
    objeto.fichaJ1 = 1
    objeto.fichaJ2 = 3
    esperado = '\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\tF\n'
    esperado += 'Raul\tI\tO\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n'
    esperado += 'Pablo\tI\t\t\tO\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF'

    cadena = objeto.pintaTablero()
    assert cadena == esperado