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


    def pintaTablero(self):
        cadena = ""
        for i in range(1, 4):
            if i == 1:
                for j in range(0, self.TAM_TABLERO+1):
                    if j == 0:
                        cadena += '\tI'
                    elif j == self.TAM_TABLERO:
                        cadena += '\tF\n'
                    else:
                        cadena += '\t' + str(j)
            elif i == 2:
                cadena += self.nombreJ1
                for j in range(0, self.TAM_TABLERO+1):
                    if self.fichaJ1 == j and self.fichaJ1 != 0:
                        cadena += '\tO'
                    elif j == 0:
                        cadena += '\tI'
                    elif j == self.TAM_TABLERO:
                        cadena += '\tF\n'
                    else:
                        cadena += '\t'

            else:
                cadena += self.nombreJ2
                for j in range(0, self.TAM_TABLERO+1):
                    if self.fichaJ2 == j and self.fichaJ2 != 0:
                        cadena += '\tO'
                    elif j == 0:
                        cadena += '\tI'
                    elif j == self.TAM_TABLERO:
                        cadena += '\tF'
                    else:
                        cadena += '\t'
        return cadena

    def avanzaPosiciones(self,turno):
        if(turno == 1):
            self.fichaJ1 += self.dado1 + self.dado2
            if self.fichaJ1 > self.TAM_TABLERO:
                self.fichaJ1 = self.TAM_TABLERO - (self.fichaJ1 - self.TAM_TABLERO)
        else:
            self.fichaJ2 += self.dado1 + self.dado2
            if self.fichaJ2 > self.TAM_TABLERO:
                self.fichaJ2 = self.TAM_TABLERO - (self.fichaJ2 - self.TAM_TABLERO)

    def estadoCarrera(self):
        ganando = ''
        if self.fichaJ1 > self.fichaJ2:
            ganando = f'{self.nombreJ1} va ganando'
        elif self.fichaJ1 < self.fichaJ2:
            ganando = f'{self.nombreJ2} va ganando'
        else:
            ganando = 'Empate, nadie va ganando'
        return ganando

    def esGanador(self):
        ganador = ''
        if self.fichaJ1 == self.TAM_TABLERO:
            ganador = self.nombreJ1
        elif self.fichaJ2 == self.TAM_TABLERO:
            ganador = self.nombreJ2
        return ganador