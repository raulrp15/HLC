from Parchis.Parchis import *

objeto = Parchis('Raul', 'Pablo')

def test_pintaTablero1():
    esperado = '\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\tF\n'
    esperado += 'Raul\tI\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n'
    esperado += 'Pablo\tI\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF'
    cadena = objeto.pintaTablero(0, 0)
    assert cadena == esperado


def test_pintaTablero2():
    esperado = '\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\tF\n'
    esperado += 'Raul\tI\tO\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n'
    esperado += 'Pablo\tI\t\t\tO\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF'

    cadena = objeto.pintaTablero(1, 3)
    assert cadena == esperado