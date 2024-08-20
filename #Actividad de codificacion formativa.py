#Actividad de codificacion formativa
#Entradas = pNumero(int)
#Salida determinar la cantidad de digitos de pNumero
#Resticciones: pNumero >0

def contarDigitos(pNumero):
    contador = 0
    while (pNumero != 0):
        pNumero = pNumero // 10 
        contador += 1  #Equivale a contador = contador +1
    return contador
res = contarDigitos(670)
print(res)

#Ejemplo 2
#Version 1 -  Probar todos los divisores
#Entradas: pNumero (int)
#Salidas: True / False, True en caso que pNumero sea primo
#Restriccienes: pNumero >= 2
#Version 1
def esPrimo(pNumero):
    contador = 0
    divisorInicial = 1
    while (True):
        if (divisorInicial > pNumero):
            break # Termina el ciclo mas interno donde se encuentra

        if (pNumero % divisorInicial == 0):
            contador = contador + 1
        divisorInicial = divisorInicial + 1

    if (contador == 2):
        return True
    else:
        return False

print(esPrimo(12))
 
#Version 2
def esPrimoOriginal(pNumero):
    contador = 0
    divisorInicial = 1
    while (divisorInicial <= pNumero):
        if(divisorInicial > pNumero):
            break # Termina el ciclo mas interno donde se encuentra

        if(pNumero % divisorInicial == 0):
            contador = contador + 1
        divisorInicial = divisorInicial + 1


    if(contador == 2):
        return True
    else:
        return False
    
print(esPrimoOriginal(11))

#Version 3
def esPrimoOriginalV3(pNumero):
    divisorInicial = 2
    while (divisorInicial < pNumero):
        if(pNumero % divisorInicial == 0):
            return False
        divisorInicial = divisorInicial + 1
    return True

print(esPrimoOriginalV3(11))

#Version 4
from math import sqrt #Me interesa una sola funcion 
def esPrimoOriginalV4(pNumero):
    divisorInicial = 2
    raizCuadrada = int(sqrt(pNumero))
    while divisorInicial <= raizCuadrada:
        if(pNumero % divisorInicial == 0):
            return False
        divisorInicial = divisorInicial + 1
    return True

print(esPrimoOriginalV4(12))

#Ejemplo Determinar la cantidad de numeros primos en un intervalo cerrado
def contarPrimos(pInicioIntervalo, pFinIntervalo):
    contador = 0 
    while (pInicioIntervalo <= pFinIntervalo):
        if(esPrimoOriginalV4(pInicioIntervalo)):
            contador = contador + 1
        pInicioIntervalo = pInicioIntervalo + 1 
    return contador
print(contarPrimos(2, 44544564464))