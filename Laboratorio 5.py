
def esPrimo(pNum):
    if pNum < 2:
        return False
    divisorInicial = 2
    while (divisorInicial < pNum):
        if(pNum % divisorInicial == 0):
            return False
        divisorInicial = divisorInicial + 1
    return True
    
def extraerDigitosEnPosicionPrima(pNum):
    posicion = 1
    resultado = 0 
    potencia = 0
    while (pNum != 0):
        if(esPrimo(posicion)):
            digito = pNum % 10
            resultado = resultado + (digito * 10 ** potencia)
            potencia += 1
        pNum = pNum // 10
        posicion += 1
    return resultado

#print(test_esPrimo())
def test_esPrimo():
    assert esPrimo (-1) == False, "Verifique porque los negativos no son primos"
    assert esPrimo(0) == False, "Cero no es un numero primo"
    assert esPrimo(1) == False, "Uno no es un numero primo"
    assert esPrimo(2) == True, "Dos es un numero primo"
    assert esPrimo(11) == True, "Once es un numero primo"
    assert esPrimo(15) == False, "Quince tiene 5 y 3 como divisores no es primo"

def formarNumero(pNum, pDigito):
    pNum = abs(pNum)
    pDigito = abs(pDigito)
    posicion = 0
    resultado = 0
    while pNum != 0:
        digitoPNum = pNum % 10
        if digitoPNum % pDigito == 0:
            resultado = resultado + (digitoPNum * 10 ** posicion)
            posicion += 1
        pNum = pNum // 10
    return resultado

def testformar_Numeros():
    assert formarNumero(791341, 5) == 0, "No existen digitos de 5 en 791341"
    assert formarNumero(-791341, 3) == 93, "Verifique escenario de numeros negativos"
    assert formarNumero(2356,2) == 26, "El 2 y 6 son multiplos de 2"
    assert formarNumero(0, 3) == 0, "Si pNum es 0 no habran multiplos del digito"
print(testformar_Numeros())

#RETO 3

def contarDigitos(pNumero):
    contador = 0
    pNumero = abs(pNumero)
    while pNumero != 0:
        pNumero = pNumero//10
        contador +=1
    return contador

def test_contarDigitos():
    assert contarDigitos(125) == 3, "125 tiene 3 digitos"
    assert contarDigitos(-125) ==3, "-125 tiene 2 digitos"

def intercambiar(pNum1, pNum2):
    if (pNum1 < 0 or pNum2 < 0) or (contarDigitos(pNum1) != contarDigitos(pNum2)):
        return 0
    posicion = 0
    resultado = 0
    while(pNum1 != 0):
        digitoPNum1 = pNum1 % 10
        digitoPNum2 = pNum2 % 10
        if(digitoPNum1 > digitoPNum2):
            resultado = resultado + (digitoPNum2 * 10 ** posicion)
        else:
            resultado = resultado + (digitoPNum1 * 10 ** posicion)
        posicion += 1
        pNum1 = pNum1 // 10
        pNum2 = pNum2 // 10
    return resultado

def test_intercambiar():
    assert intercambiar(765, 1312) == 0, "pNum1 y pNum2 deben de tener la misma cantidad de digitos"
    assert intercambiar(-115,345) == 0, "La funcion no trabaja con numero negativos"
    assert intercambiar(1258, 4167) == 1157, "Verifique el caso numero 3"
print(test_intercambiar())





def existeDigitos(digitospNum, pNum):
    digitospNum = abs(digitospNum)
    pNum = abs(pNum)
    while(pNum != 0):
        if(pNum % 10 == digitospNum):
            return True
        pNum = pNum // 10
    return False
#print(existeDigitos(4, 4845))

def test_existeDigitos():
    assert existeDigitos(4, 4848) == True, "El digito de 4 se encuentra en 4848"
    assert existeDigitos(-1, 1245) == True, "El digito de 1 esta presente en 1245"
    assert existeDigitos(5, 8798) == False, "El digito de 5 no se encuentra en 8798"
    assert existeDigitos(5, -5655)== True, "El digito 5 se encuentra en -5655"
#print(test_existeDigitos())


def diferenciarDigitos(pNum1, pNum2):
    pNum1 = abs(pNum1)
    pNum2 = abs(pNum2)
    potencia = 0
    resultado = 0
    while (pNum1 != 0):
        if(existeDigitos(pNum1 % 10, pNum2)== False):
            resultado = resultado + ((pNum1 % 10)*10**potencia)
            potencia += 1
        pNum1 = pNum1 // 10
    return resultado
#print(diferenciarDigitos(8596, 5621))

def test_diferenciarDigitos():
    assert diferenciarDigitos(8596, 5621) == 89, "En los numeros a= 8596 y b= 5621 solo el 8 y 9 estan solo a y no en b"
    assert diferenciarDigitos(-1524, 5646)== 12, "En los numeros a=-1524 y b= 5646 solo el 1 y 2 estan solo en a y no en b"
    assert diferenciarDigitos(1524, -5646)== 12, "En los numeros a=-1524 y b= 5646 solo el 1 y 2 estan solo en a y no en b"
    assert diferenciarDigitos(454, 897)== 454, "En los numeros a= 454 y b= 897 todos los numeros de a no estan en b"
    assert diferenciarDigitos(55, 54)== 0, "En los numeros a= 55 y b= 55 todos los numeros de a estan en b"
print(test_diferenciarDigitos())

    