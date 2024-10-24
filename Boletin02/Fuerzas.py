def CalculoFuerzas(datoP, datoS):
    resultado = ""
    dato1 = datoP.split("=")
    dato2 = datoS.split("=")
    n1 = int(dato1[1])
    n2 = int(dato2[1])

    if dato1[0] == 'D' and dato2[0] == 'T':
        if n2 != 0:
            v = int(n1 / n2)
            resultado = f"V={v}"
        else:
            resultado = "No se puede dividir entre 0"
    elif dato1[0] == 'T' and dato2[0] == 'D':
        if n1 != 0:
            v = int(n2 / n1)
            resultado = f"V={v}"
        else:
            resultado = "No se puede dividir entre 0"
    elif dato1[0] == 'V' and dato2[0] == 'T':
        d = int(n1 * n2)
        resultado = f"D={d}"
    elif dato1[0] == 'T' and dato2[0] == 'V':
        d = int(n2 * n1)
        resultado = f"D={d}"
    elif dato1[0] == 'V' and dato2[0] == 'D':
        if n1 != 0:
            t = int(n2 / n1)
            resultado = f"T={t}"
        else:
            resultado = "No se puede dividir entre 0"
    elif dato1[0] == 'D' and dato2[0] == 'V':
        if n2 != 0:
            t = int(n1 / n2)
            resultado = f"T={t}"
        else:
            resultado = "No se puede dividir entre 0"
    else:
        return "Datos no válidos"
        
    return resultado