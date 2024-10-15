abecedario = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

def cifCesar(clave, palabra):
    palabraCifrada = ""
    for letra in palabra:
        if letra == " ":
            palabraCifrada += " "
        else:
            posicionLetra = abecedario.index(letra)
        
            if (posicionLetra + clave) >= len(abecedario):
                posicionNueva = clave - (27%posicionLetra)
                palabraCifrada += abecedario[posicionNueva]
            else:
                posicionNueva = posicionLetra + clave
                palabraCifrada += abecedario[posicionNueva]
    return palabraCifrada

# Tupla len 27 [0-26]
# x = 24 --> a = 0 || Clave = 3