import random
class Ahorcado:
    NUMINTENTOS = 7
    palabras = ["humanidad", "persona", "hombre", "mujer", "individuo", "cuerpo", "pierna", "cabeza", "brazo", "familia"]
    def __init__(self):
        self.noAcertadas = ""
        self.palabraSecreta = ""
        self.palabraPista = ""

    def generaPalabras(self):
        self.palabraSecreta = self.palabras[random.randint(0, len(self.palabras)-1)]
        self.palabraPista += '_' * len(self.palabraSecreta)

    def compruebaLetra(self, letra):
        letraC = letra.lower()
        palabra = list(self.palabraSecreta)
        palabraP = list(self.palabraPista)
        if self.palabraSecreta.__contains__(letraC):
            for i in range(0, len(palabra)):
                if palabra[i] == letraC:
                    palabraP[i] = letraC
                    self.palabraPista = ""
            for letras in palabraP:
                
                self.palabraPista += letras
        else:
            self.noAcertadas += f' {letraC}'