from Parchis import Parchis


esperado = '\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\tF\n'
esperado += 'Raul\tI\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n'
esperado += 'Pablo\tI\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF'

prueba = Parchis('Raul', 'Pablo')

print(prueba.pintaTablero(0, 0))
print(esperado)