import random


class Parchis:
    TAM_TABLERO = 20
    dado1 = 0
    dado2 = 0

    def __init__(self, nombreJ1, nombreJ2):
        self.fichaJ1 = 0
        self.fichaJ2 = 0
        self.nombreJ1 = nombreJ1
        self.nombreJ2 = nombreJ2

    def tiraDados():
        Parchis.dado1 = random.randint(1, 6)
        Parchis.dado2 = random.randint(1, 6)


    def pintaTablero(self, fichaJ1, fichaJ2):
        cadena = ""
        for i in range(1, 4):
            if i == 1:
                for j in range(0, Parchis.TAM_TABLERO+1):
                    if j == 0:
                        cadena += '\tI'
                    elif j == Parchis.TAM_TABLERO:
                        cadena += '\tF\n'
                    else:
                        cadena += '\t' + str(j)
            elif i == 2:
                cadena += self.nombreJ1
                for j in range(0, Parchis.TAM_TABLERO+1):
                    if fichaJ1 == j and fichaJ1 != 0:
                        cadena += '\tO'
                    elif j == 0:
                        cadena += '\tI'
                    elif j == Parchis.TAM_TABLERO:
                        cadena += '\tF\n'
                    else:
                        cadena += '\t'

            else:
                cadena += self.nombreJ2
                for j in range(0, Parchis.TAM_TABLERO+1):
                    if fichaJ2 == j and fichaJ2 != 0:
                        cadena += '\tO'
                    elif j == 0:
                        cadena += '\tI'
                    elif j == Parchis.TAM_TABLERO:
                        cadena += '\tF'
                    else:
                        cadena += '\t'
        return cadena