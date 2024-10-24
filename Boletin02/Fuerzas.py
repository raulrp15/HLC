def CalculoFuerzas(datoP, datoS):
    dato1 = datoP.split("=")
    dato2 = datoS.split("=")
    if dato1[0] == "D" and dato2[0] == "T":
        resultado = "V" + (dato1[1] + dato2[1])
    return resultado