#Ejemplo#1
#Entradas = pNumero (int)
#Salidas = La cantidad de digitos que forman pNumero (int)
#Restricciones = pNumero > 0 (la funcion NO debe validar restricciones)
def contarDigitos(pNum):
    contador = 0
    while (pNum != 0):
        pNum = pNum//10
        contador += 1
    return contador
print(f"La cantidad de digitos es de {contarDigitos(7328)}")

#Ejemplo#2
#Entrada = pNumero (int)
#Salida = El producto de todos los numeros enteros desde 1 hasta pNum
def determinarFactorial(pNum):
    inicio = 1
    factorial = 1
    while(inicio <= pNum):
        factorial = inicio * factorial
        inicio += 1
    return factorial
print(f"El producto de pNum Factorial es de: {determinarFactorial(5)}")

#Ejemplo#3
#Entradas = pNum (int) 
#Salida = El valor de pNum invertido de derecha a izquierda
#Restricciones = pNum > 0
def invertirNumero(pNum):
    while (pNum > 10):
        resultado = 0
        potencia = contarDigitos(pNum)-1
        while (pNum != 0):
            ultimoDigito = pNum % 10
            reposicionarDigito = ultimoDigito * (10**potencia)
            resultado = reposicionarDigito + resultado
            pNum = pNum // 10
            potencia = potencia - 1
        return resultado
    return(pNum)       
print(f"El numero invertido es: {invertirNumero(3561)}")

#Ejemplo#4
#Entradas = pNum: Un número entero mayor a 1
#Salidos = True: Si pNum tiene únicamente 2 divisores (1 y pNum) False: En caso que pNum tenga 3 o más divisores
#Restricciones = pNum (int) > 0
def determinarPrimalidad(pNum):
    divisorInicial = 2
    while (divisorInicial < pNum):
        if(pNum % divisorInicial == 0):
            return False
        divisorInicial += 1
    return True
print(f"{determinarPrimalidad(7)}")

#Reto estudiante
#Entradas= pNum (int)
#Salidas = La suma de los digitos de pNum
#Restricciones = pNum > 0
def sumarDigitos(pNumero):
    resultado = 0
    while (pNum != 0):
        ultimoDigito = pNum % 10
        resultado = ultimoDigito + resultado
        pNum = pNum // 10
    return resultado
print(sumarDigitos(61025))


