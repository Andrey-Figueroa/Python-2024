import sys
sys.setrecursionlimit(150000)

#RETO1: Sumar dígitos múltiplos
#Entradas: pNum(int), pDig(int), la función recibe un número y un digito
#Salidas: resultado(int), suma de todos sus dígitos, siempre y cuando esos dígitos sean múltiplos del dígito especificado por el segundo parámetro. 
#Restricciones: pNum debe ser un entero positivo mayor que cero
def sumarDigitosMultiplos(pNum, pMultiplo):
    return sumarDigitosMultiplosAux(pNum,pMultiplo, 0)
def sumarDigitosMultiplosAux(pNum, pMultiplo, acumulador):
    if pNum == 0:
        return acumulador
    if (pNum % 10) % pMultiplo == 0:
        return sumarDigitosMultiplosAux(pNum // 10, pMultiplo, acumulador + (pNum % 10))
    else:
        return sumarDigitosMultiplosAux(pNum // 10, pMultiplo, acumulador)

#RETO2: Formar un número con los dígitos pares de otro número
#Entradas: pNum(int), recibe un numero entero
#Salidas: resultado(int), numero formado a partir de los digitos pares de pNum
#Restricciones: pNum debe ser un numero entero
def formarNumero(pNum):
    return formarNumeroAux(pNum,0,1)
def formarNumeroAux(pNum, acumulador, factor):
    pNum = abs(pNum)
    if pNum == 0:
        return acumulador
    if (pNum % 10) % 2 == 0:
        return formarNumeroAux(pNum // 10, acumulador + (pNum % 10) * factor, factor * 10)
    else:
        return formarNumeroAux(pNum // 10, acumulador, factor)

#RETO3: Elevar un número a una potencia dada
#Entradas: pNum(int),pPotencia(int)
#Salidas: resultado(int), pNum elevado a pPotencia
#Restriccion: pNum y pPotencia deben ser enteros positivos mayores o iguales que cero
def elevar(pNum,pPotencia):
    return elevarAux(pNum,pPotencia,1)

def elevarAux(pNum,pPotencia,resultado):
    if(pPotencia == 0):
        return resultado
    return elevarAux(pNum, pPotencia - 1,resultado * pNum)

#RETO4: Binario a decimal
#Entradas: pBinario(int), potencia=0
#Salidas: resultado(int) representación decimal.
#Restricción: que pBinario contenga base binaria
def convertirADecimal(pBinario):
    return convertirADecimalAux(pBinario, 0, 0)
def convertirADecimalAux(pBinario, potencia, resultado):
    if pBinario == 0:
        return resultado
    return convertirADecimalAux(pBinario // 10, potencia + 1, resultado + (pBinario % 10) * (2 ** potencia))

#RETO5: Sumatoria Recursiva
#Entradas: pParada(int), indice=0(int), acumulador=0(int)
#Salida: resultado(int) resultado de la sumatoria
#Restricciones: pParada debe ser (int) y pParada > 0
def sumatoriaRecursividad(pParada):
    return sumatoriaRecursivaAux(pParada,0)
def sumatoriaRecursivaAux(pParada,resultado):
    if pParada < 0:
        return resultado
    return sumatoriaRecursivaAux(pParada-1,resultado + pParada) 

#RETO6: Eliminar Repetidos
#Entradas: pLista(list)
#Salida: respuesta(list) nueva lista donde sus elementos son únicos
#Restriccion: Si la lista está vacía, la función debe retornar []
def existeElemento(pLista,pElemento):
    if(pLista == []):
        return False
    if(pLista[0] == pElemento):
        return True
    else:
        return existeElemento(pLista[1:],pElemento)
        
def eliminarRepetidos(pLista):
    return eliminarRepetidosAux(pLista,[])
def eliminarRepetidosAux(pLista,resultado):
    if (pLista == []):
        return resultado
    if(existeElemento(pLista[1:],pLista[0])):
        return eliminarRepetidosAux(pLista[1:],resultado)
    else:
        return eliminarRepetidosAux(pLista[1:],resultado + [pLista[0]])

#RETO7: Intersección
#Entradas: pLista1(list), pLista2(list), la función debe recibir dos listas
#Salidas: interseccion(list) la función retorna la intersección de las listas
#Restricciones: pLista2 != [] para que pueda realizar alguna operacion
def interseccion(pLista1,pLista2):
    return interseccionAux(pLista1, pLista2,[])
def interseccionAux(pLista1, pLista2,resultado):
    if(pLista1 == []):
        return resultado
    if(existeElemento(pLista2,pLista1[0])):
        return  interseccionAux(pLista1[1:],pLista2,resultado + [pLista1[0]])
    else:
        return interseccionAux(pLista1[1:],pLista2,resultado)

#RETO8: diferencia
#Entradas: pLista1(list), pLista2(list), la función debe recibir dos listas
#Salidas: diferencia(list) la función retorna la diferencia de las listas
#Restricciones: pLista2 != [] para que pueda realizar alguna operacion
def diferencia(pLista1,pLista2):
    return diferenciaAux(pLista1, pLista2,[])
def diferenciaAux(pLista1, pLista2,resultado):
    if(pLista1 == []):
        return resultado
    if(existeElemento(pLista2,pLista1[0]) == False):
        return diferenciaAux(pLista1[1:],pLista2,resultado + [pLista1[0]])
    else:
        return diferenciaAux(pLista1[1:],pLista2,resultado)

#RETO9: Suma sucesiva
#Entradas: pLista(list) la función recibe una lista de numeros
#Salida: listaAcumulada(list), lista que devuelva la suma acumulada
#Restricciones: los numeros de la lista deben ser enteros
def sumaSucesiva(pLista):
    return sumaSucesivaAux(pLista, 0)
def sumaSucesivaAux(pLista, acumulador):
    if pLista == []:
        return []
    nuevoValor = acumulador + pLista[0]
    resultado = sumaSucesivaAux(pLista[1:], nuevoValor)
    return [nuevoValor] + resultado 

#RETO10: eliminarCaracter
#Entradas: pCadena(str),caracter(str), La funcion debe recibir una cadena de caracteres y un carácter
#Salidas: nuevaCadena(str), La función debe eliminar las apariciones del carácter indicado de la cadena y retornar la nueva cadena
#Restricciones: Ambas entradas deben ser str
def eliminarCaracter(pCadena,caracter):
    return eliminarCaracterAux(pCadena,caracter,"")
def eliminarCaracterAux(pCadena,caracter,resultado):
    if(pCadena == ""):
        return resultado
    if(caracter != pCadena[0]):
        return eliminarCaracterAux(pCadena[1:],caracter,resultado + pCadena[0])
    return eliminarCaracterAux(pCadena[1:],caracter,resultado)

#RETO11: Primos Lista
#Entradas: pLista(list) Recibe una lista de números enteros
#Salidas: primosLista(list) La función retorna otra lista que únicamente contenga los números primos
#Restricciones: los elementos de pLista deben ser enteros, En caso que la lista esté vacía, debe retornar []
def esPrimo(pNum):
    if pNum < 2:
        return False
    return esPrimoAux(pNum, 2)
def esPrimoAux(pNum, divisor):
    if divisor * divisor > pNum:
        return True
    if pNum % divisor == 0:
        return False
    return esPrimoAux(pNum, divisor + 1)

def primosLista(pLista):
    return primosListaAux(pLista,[])
def primosListaAux(pLista,resultado):
    if(pLista == []):
        return resultado
    if(esPrimo(pLista[0])):
        return primosListaAux(pLista[1:],resultado + [pLista[0]])
    return primosListaAux(pLista[1:],resultado)

#Reto12: Producto cartesiano
#Entradas: pLista1(list), pLista2(list), la función debe recibir dos listas
#Salidas: nuevaLista(list) da como salida el producto cartesiano de pLista1 y pLista2
#Restricciones: ambas entradas deben ser list, no str
def combinar(pElemento,pLista):
    return combinarAux(pElemento, pLista, [])
def combinarAux(pElemento, pLista, resultado):
    if pLista == []:
        return resultado
    return combinarAux(pElemento,pLista[1:],resultado + [[pElemento,pLista[0]]] )

def productoCartesiano(pLista1, pLista2):
    return productoCartesianoAux(pLista1,pLista2,[])

def productoCartesianoAux(pLista1,pLista2,resultado):
    if(pLista1 == []):
        return resultado
    return productoCartesianoAux(pLista1[1:],pLista2,resultado + combinar(pLista1[0],pLista2))

#RETO13: Sucesión de ULAM
#Entradas: pNum(int) numero de inicio para la sucesión
#Salidas: sucesion(list) la función retorna la sucesión de Ulam 
#Restricciones: pNum debe ser un número entero positivo mayor que 0
def sucesionULAM(pNum):
    return sucesionUlamAux(pNum,[])
def sucesionUlamAux(pNum,resultado):
    if(pNum == 1):
        return resultado + [1]
    resultado.append(pNum)
    if(pNum % 2 == 0):
        return sucesionUlamAux(pNum//2,resultado)
    else:
        return sucesionUlamAux((pNum*3)+1,resultado)

#RETO14: Contar cantidad de caracteres
#Entradas: pCadena(str) la función recibe como entrada una cadena de caracteres
#Salidas: cantidadCaracteres(list)
#Restricciones: la entrada debe ser str
def contarCaracter(pCadena,caracter):
    return contarCaracterAux(pCadena, caracter, 0)
def contarCaracterAux(pCadena, caracter, contador):
    if(pCadena == ""):
        return contador
    if(caracter == pCadena[0]):
        return contarCaracterAux(pCadena[1:],caracter,contador + 1)
    return contarCaracterAux(pCadena[1:],caracter,contador)

def contarCarateresCadena(pCadena):
    return contarCaracteresCadenaAux(pCadena,[])
def contarCaracteresCadenaAux(pCadena, resultado):
    if pCadena == "":
        return resultado
    caracter = pCadena[0]
    cuenta = contarCaracter(pCadena, caracter)
    pCadena = eliminarCaracter(pCadena, caracter)
    return contarCaracteresCadenaAux(pCadena, resultado + [[caracter, cuenta]])