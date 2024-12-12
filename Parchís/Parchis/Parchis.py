import random


class Parchis:
#region Atributos
    TAM_TABLERO = 20
    dado1 = 0
    dado2 = 0
#endregion

#region Constructor

    '''
    Metodo que sirve de constructor de la clase
    Inicializa la posicion de las fichas a 0 y 
    los nombres de los jugadores que se inserten en el main
    @Param nombreJ1, Nombre del jugador 1
    @Param nombreJ2, Nombre del jugador 2
    '''
    def __init__(self, nombreJ1, nombreJ2):
        self.fichaJ1 = 0
        self.fichaJ2 = 0
        self.nombreJ1 = nombreJ1
        self.nombreJ2 = nombreJ2
#endregion

#region Metodos
    '''
    Metodo que simula el tiro de los dados
    '''
    def tiraDados():
        Parchis.dado1 = random.randint(1, 6)
        Parchis.dado2 = random.randint(1, 6)

    '''
    Metodo que pinta el tablero
    @Return cadena, Cadena con el tablero pintado con las fichas 
    '''
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

    '''
    Metodo que avanza las fichas de los jugadores
    @Param turno, Turno del jugador
    '''
    def avanzaPosiciones(self,turno):
        if(turno == 1):
            self.fichaJ1 += self.dado1 + self.dado2
            if self.fichaJ1 > self.TAM_TABLERO:
                self.fichaJ1 = abs(self.TAM_TABLERO - (self.fichaJ1 - self.TAM_TABLERO))
        else:
            self.fichaJ2 += self.dado1 + self.dado2
            if self.fichaJ2 > self.TAM_TABLERO:
                self.fichaJ2 = abs(self.TAM_TABLERO - (self.fichaJ2 - self.TAM_TABLERO))

    '''
    Metodo que determina el ganador de la partida
    @Return ganador, Nombre del jugador que va ganando
    '''
    def estadoCarrera(self):
        ganando = ''
        if self.fichaJ1 > self.fichaJ2:
            ganando = self.nombreJ1
        elif self.fichaJ1 < self.fichaJ2:
            ganando = self.nombreJ2
        else:
            ganando = 'Empate'
        return ganando

    '''
    Metodo que determina el ganador de la partida
    @Return ganador, Nombre del jugador que ha ganado
    '''
    def esGanador(self):
        ganador = ''
        if self.fichaJ1 == self.TAM_TABLERO:
            ganador = self.nombreJ1
        elif self.fichaJ2 == self.TAM_TABLERO:
            ganador = self.nombreJ2
        return ganador
#endregion