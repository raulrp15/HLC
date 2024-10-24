def Kaprekar(numero):
    vueltas = 0
    while numero != 6174 and vueltas <= 7:
        num = str(numero)
        lista = list(num)
        if len(lista) < 4:
            lista += '0' * (4 - len(lista))
        lista.sort()
        asc = 0
        for i in range(4):
            asc = asc * 10 + int(lista[i])
        lista.sort()
        desc = 0
        for i in range(3, -1, -1):
            desc = desc * 10 + int(lista[i])
        if asc == desc:
            vueltas = 8
            break;
        numero = abs(desc - asc)
        vueltas += 1
    return vueltas