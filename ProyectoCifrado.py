#CIFRADO CESAR
def cambiarLetraCesar(pLetra):
    abecedarioCesar = "DEFGHIJKLMNOPQRSTUVWXYZABC"
    posicionLetra = ord(pLetra) - ord('A') #Nos da la posicion de pLetra en el abecedario
    letra = abecedarioCesar[posicionLetra]
    return letra

def codificarCesar(pCadena):
    if not isinstance(pCadena, str):
        return "Cadena invalida, debe ser una cadena de texto."
    if(pCadena == ""):
        return "Cadena invalida, la cadena no puede estar vacia."
    pCadena = pCadena.upper()
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cifrado = ""
    for pLetra in pCadena:
        if(pLetra in abecedario):
            nuevaLetra = cambiarLetraCesar(pLetra)
            cifrado += nuevaLetra
        else:
            cifrado += pLetra
    return cifrado

#DESCIFRADO CESAR
def descifrarMayuscula(pLetra):
    abecedarioCesar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    posicionLetra = ord(pLetra) - ord('A') #Nos da la posicion de pLetra en el abecedario
    letra = abecedarioCesar[(posicionLetra-3)% 26] 
    return letra

def descifrarMinisculas(pLetra):
    abecedario = "abcdefghijklmnopqrstuvwxyz"
    posicionLetra = ord(pLetra) - ord('a') #Nos da la posicion de pLetra en el abecedario
    letra = abecedario[(posicionLetra-3)% 26] 
    return letra

def descodificarCesar(pCadena):
    if not isinstance(pCadena, str):
        return "Cadena invalida, debe ser una cadena de texto."
    if(pCadena == ""):
        return "Cadena invalida, la cadena no puede estar vacia."
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    descifrado = ""
    for pLetra in pCadena:
        if (pLetra in abecedario):
            if (pLetra.islower()):
                nuevaLetra = descifrarMinisculas(pLetra)
                descifrado += nuevaLetra
            elif (pLetra.isupper()):
                nuevaLetra = descifrarMayuscula(pLetra)
                descifrado += nuevaLetra
        else:
            descifrado += pLetra #¿Solo permite letras?
    return descifrado


#CIFRADO Sustitución Vigenére
def cifrarVigenére(pLetra,pNumero):
    abecedario = "abcdefghijklmnopqrstuvwxyz"
    posicionLetra = ord(pLetra) - ord('a') #Nos da la posicion de pLetra en el abecedario
    letra = abecedario[(posicionLetra + pNumero)% 26] 
    return letra

def codificarVigenere(pCadena,pCifra):
    if not isinstance(pCadena, str):
        return "Cadena invalida, debe ser una cadena de texto."
    if(pCadena == ""):
        return "Cadena invalida, la cadena no puede estar vacia."
    if(pCifra < 10 or pCifra > 99):
        return "La cifra de codificación debe tener 2 digitos"
    cifrado = ""
    pCadena = pCadena.lower()
    abecedario = "abcdefghijklmnopqrstuvwxyz"
    indice = 0
    while(indice < len(pCadena)):
        if(pCadena[indice] in abecedario):
                if((indice+1) % 2 == 1):
                    nuevaLetra = cifrarVigenére(pCadena[indice],pCifra // 10)
                    cifrado += nuevaLetra
                else:
                    nuevaLetra = cifrarVigenére(pCadena[indice],pCifra % 10)
                    cifrado += nuevaLetra       
        else:
            cifrado += pCadena[indice]
        indice += 1
    return cifrado

#DESCIFRADO Sustitución Vigenére
def descifrarVigenére(pLetra,pNumero):
    abecedario = "abcdefghijklmnopqrstuvwxyz"
    posicionLetra = ord(pLetra) - ord('a') #Nos da la posicion de pLetra en el abecedario
    letra = abecedario[(posicionLetra - pNumero)% 26] 
    return letra

def descodificarVigenere(pCadena,pCifra):
    if not isinstance(pCadena, str):
        return "Cadena invalida, debe ser una cadena de texto."
    if(pCadena == ""):
        return "Cadena invalida, la cadena no puede estar vacia."
    if(pCifra < 10 or pCifra > 99):
        return "La cifra de codificación debe tener 2 digitos"
    cifrado = ""
    pCadena = pCadena.lower()
    abecedario = "abcdefghijklmnopqrstuvwxyz"
    indice = 0
    while(indice < len(pCadena)):
        if(pCadena[indice] in abecedario):
                if((indice+1) % 2 == 1):
                    nuevaLetra = descifrarVigenére(pCadena[indice],pCifra // 10)
                    cifrado += nuevaLetra
                else:
                    nuevaLetra = descifrarVigenére(pCadena[indice],pCifra % 10)
                    cifrado += nuevaLetra       
        else:
            cifrado += pCadena[indice]  #¿Solo permite letras?
        indice += 1
    return cifrado


#CIFRADO Mensaje Inverso
def invertirCadena(pCadena):
    if not isinstance(pCadena, str):
        return "Cadena invalida, debe ser una cadena de texto."
    if(pCadena == ""):
        return "Cadena invalida, la cadena no puede estar vacia."
    cadenaInvertida = ""
    while(pCadena != ""):
        ultimaLetra = pCadena[-1]
        cadenaInvertida += ultimaLetra
        pCadena = pCadena[:-1]
    return cadenaInvertida

#DESCIFRADO Mensaje Inverso
def desinvertir(pCadena):
    if not isinstance(pCadena, str):
        return "Cadena invalida, debe ser una cadena de texto."
    if(pCadena == ""):
        return "Cadena invalida, la cadena no puede estar vacia."
    cadenaInvertida = ""
    while(pCadena != ""):
        ultimaLetra = pCadena[-1]
        cadenaInvertida += ultimaLetra
        pCadena = pCadena[:-1]
    return cadenaInvertida


#CIFRADO por código telefónico  / Que sucede si en la cadena nos ingresan un numero 
def codificarPorCodigoTelefonico(pCadena):
    if not isinstance(pCadena, str):
        return "Cadena invalida, debe ser una cadena de texto."
    if(pCadena == ""):
        return "Cadena invalida, la cadena no puede estar vacia."
    telefono = {
        'A': '21', 'B': '22', 'C': '23','D': '31', 'E': '32', 'F': '33',
        'G': '41', 'H': '42', 'I': '43','J': '51', 'K': '52', 'L': '53',
        'M': '61', 'N': '62', 'O': '63','P': '71', 'Q': '72', 'R': '73', 
        'S': '74','T': '81', 'U': '82', 'V': '83','W': '91', 'X': '92', 
        'Y': '93', 'Z': '94'
    }
    codigo = ""
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pCadena = pCadena.upper()
    for caracter in pCadena:
        if(caracter in letras):
            codigo += telefono[caracter] + " "
        elif(caracter == " "):
            codigo += "*"
        else:
            codigo += caracter
    return codigo

#DESCIFRADO por codigo telefonico /   FALTA HACERLO MAS ROBUSTO   / FALTA IMPLEMENTAR EL ESPACIO
def descodificarPorCodigoTelefonico(pCadena):
    pCadena = str(pCadena)
    if not pCadena.isdigit():
        return "Cadena invalida, debe ser una cadena de texto."
    if(pCadena == ""):
        return "Cadena invalida, la cadena no puede estar vacia."
    telefonoInvertido = {
    '21': 'A', '22': 'B', '23': 'C', '31': 'D', '32': 'E', '33': 'F',
    '41': 'G', '42': 'H', '43': 'I', '51': 'J', '52': 'K', '53': 'L',
    '61': 'M', '62': 'N', '63': 'O', '71': 'P', '72': 'Q', '73': 'R',
    '74': 'S', '81': 'T', '82': 'U', '83': 'V', '91': 'W', '92': 'X',
    '93': 'Y', '94': 'Z'
    }
    codigo = ""
    numeros = "0123456789"
    while(pCadena != ""):
        if(pCadena[:2] in telefonoInvertido):
            codigo += telefonoInvertido[pCadena[:2]]
            pCadena = pCadena[2:]
        else:
            codigo += " "
            pCadena = pCadena[1:]
    return codigo.lower()

x = ("tarea programada criptografia de datos zygalski Henry")
#print(codificarPorCodigoTelefonico(x))
x = 2162327432
#print(descodificarPorCodigoTelefonico(x))

#CIFRADO por Codificación Binaria (Francis Bacon, Siglo XVI)
def codificarPorBinaria(pCadena):
    binario = {
        'a': '00000', 'b': '000001', 'c': '00010','d': '00011', 'e': '00100', 'f': '00101',
        'g': '00110', 'h': '00111', 'i': '01000','j': '01001', 'k': '01010', 'l': '01011',
        'm': '01100', 'n': '01101', 'o': '01110','p': '01111', 'q': '10000', 'r': '10001', 
        's': '10010','t': '10011', 'u': '10100', 'v': '10101','w': '10110', 'x': '10111', 
        'y': '11000', 'z': '11001'
    }
    codigo = ""
    letras = "abcdefghijklmnopqrstuvwxyz"
    pCadena = pCadena.lower()
    for caracter in pCadena:
        if(caracter in letras):
            codigo += binario[caracter]
        elif(caracter == " "):
            codigo += "*"
        else:
            codigo += caracter
    return codigo
x = ("tarea programada")
#print(codificarPorBinaria(x))

#CIFRADO por Codificación Binaria V.2 (Francis Bacon, Siglo XVI)
def codificacionBinaria(pCadena):
    if  pCadena.isdigit():
        return "Cadena invalida, debe ser una cadena de texto."
    if not isinstance(pCadena, str):
        return "Cadena invalida, debe ser una cadena de texto."
    if(pCadena == ""):
        return "Cadena invalida, la cadena no puede estar vacia."
    binario = {'a': '00000', 'b': '000001', 'c': '00010','d': '00011', 'e': '00100', 'f': '00101',
        'g': '00110', 'h': '00111', 'i': '01000','j': '01001', 'k': '01010', 'l': '01011',
        'm': '01100', 'n': '01101', 'o': '01110','p': '01111', 'q': '10000', 'r': '10001', 
        's': '10010','t': '10011', 'u': '10100', 'v': '10101','w': '10110', 'x': '10111', 
        'y': '11000', 'z': '11001', ' ':'*'}
    codificacion = ''
    pCadena = pCadena.lower()
    while(pCadena != ''):
        if(pCadena[0] in binario):
            codigo = binario[pCadena[0]]
            codificacion += codigo + " "
            pCadena = pCadena[1:]
    return codificacion.strip()

    if(x == y):
        return True
    return False


#CIFRADO RSA
#CALCULAR DOS NÚMEROS PRIMOS ALEATORIOS (p, q)
from sympy import mod_inverse
import random


def esPrimo(pNumero):

    divisores = 2
    while(divisores < pNumero):
        if(pNumero % divisores == 0):
            return False
        divisores += 1
    return True

def crearNumeroPrimo(bits):
    while True:
        x = random.getrandbits(bits)
        if (esPrimo(x)):
            return x    

def maximoComunDivisor(pNum1, pNum2):
    while(pNum2 != 0):
        pNum1, pNum2 = pNum2, pNum1 % pNum2
    return pNum1

def clavesRSA(bits):
    numero1 = crearNumeroPrimo(bits)
    numero2 = crearNumeroPrimo(bits)
    n = numero1 * numero2
    euler = (numero1 - 1) * (numero2 - 1)
    while(True):
        e = random.randrange(2, euler)   #GENERA ERROR AVECES
        if(maximoComunDivisor(e, euler) == 1):
            break
    d = mod_inverse(e,euler)
    return [e,n,d]
print(clavesRSA(8))

def buscarPosicion(pCadena):
    posicion = 0
    while(pCadena != ""):
        if(pCadena[0] == "*"):
            return posicion
        pCadena = pCadena[1:]
        posicion += 1
    return posicion 

def codificarRSA(pCadena):
    criptado = ""
    llaves = clavesRSA(7)
    for letra in pCadena:
        valorLetra = ord(letra)
        letraCriptada = (valorLetra ** llaves[0]) % llaves[1]
        criptado += str(letraCriptada) + "*"
    print (criptado)
    descriptado = ""

    while(criptado != ""):
        posicionAsterisco = buscarPosicion(criptado) 
        palabra = criptado[:posicionAsterisco]
        letraCriptada = (int(palabra) ** llaves[2]) % llaves[1]
        descriptado += chr(letraCriptada)
        criptado = criptado[posicionAsterisco+1:]
    print(descriptado)

print(codificarRSA("Hola"))

def descodificarRSA(pCadena):
    descriptado = ""
    llaves = clavesRSA(7)
    while(pCadena != ""):
        posicionAsterisco = buscarPosicion(pCadena) 
        palabra = pCadena[:posicionAsterisco]
        letraCriptada = (int(palabra) ** llaves[2]) % llaves[1]
        descriptado += chr(letraCriptada)
        pCadena = pCadena[posicionAsterisco+1:]
    return descriptado


#Criptado por llave
def posicionLetra(letra):
    letra = letra.lower()
    posicion = ord(letra)-ord("a")+1
    return posicion

def nuevaLetraPorClave(pLetra1,pLetra2):
    posicion1 = posicionLetra(pLetra1)
    posicion2 = posicionLetra(pLetra2)
    nuevaLetra = posicion1 + posicion2
    if(nuevaLetra >= 26):
        nuevaLetra -= 26
    letras = "abcdefghijklmnopqrstuvwxyz"
    nuevaLetra = letras[nuevaLetra-1]
    return nuevaLetra

def codificarPorClave(pCadena,pClave):
    criptado = ""
    indice = 0
    for letra in pCadena:
        if(indice >= len(pClave)):
            indice = 0
        if(letra != " "):
            letraNueva = nuevaLetraPorClave(letra,pClave[indice])
            criptado += letraNueva
            indice += 1
        else:
            criptado += " "
            indice = 0
    return criptado
x = "programada"
y = "Tango"
print(codificarPorClave(x,y))
        


