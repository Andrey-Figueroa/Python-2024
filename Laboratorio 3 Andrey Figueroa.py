#Andrey Figueroa Calderón 
#Laboratorio 2
#Primeros pasos en codificación

#Ejemplo #1
#Entradas: numero (int)
#Salidas: cadena (str)
#Restricciones.


def determinarParidad():
    print("Indique el numero a determinar: ")
    numero = int(input())
    if(numero%2 == 0):
        print("El numero->", numero, "es par")
    else:
        print("El numero->", numero, "es impar")

determinarParidad()

#Ejemplo #2
#Entradas: edad(int)
#Salidas: cadena(str)
#Restricciones: edad numero entero, edad > 0
def determinarMayoriaEdad():
    edad = int(input("Indique su edad: "))
    if edad >= 18:
        print("Eres mayor de edad")

determinarMayoriaEdad()
#Ejemplo #3
#Entradas: numero entero (int)
#Salidas: cadena(str) "El numero es positivo", "El numero es negativo"
#Restricciones: numero debe ser int 
def determinarNegativoPositivo():
    numero = int(input("Indique el numero que desee determinar: "))
    if (numero >= 0):
        print("El numero ", numero, " es positivo.")
    else:
        print("El numero ", numero, " es negativo.")

determinarNegativoPositivo()

#Ejemplo #4
#Entradas: puntaje (float)
#Salidas: cadena(str) A, B, C, D, F
#Restricciones: puntaje >= 0 and puntaje <= 10

def calcularCalificacion():
    puntaje = float(input("Indique su nota: "))
    if (puntaje >= 90):
        print("A")
    else:
        if(puntaje >= 80):
            print("B")
        else:
            if(puntaje >= 70):
                 print("C")
            else:
                if(puntaje >= 60):
                    print("D")
                else:
                    print("F")

calcularCalificacion()

def calcularCalificacionV2():
    puntaje = float(input("Indique su nota: "))
    if (puntaje >= 90):
        print("A")
    elif(puntaje >= 80):
        print("B")
    elif(puntaje >= 70):
         print("C")
    elif(puntaje >= 60):
        print("D")
    else:
        print("F")

calcularCalificacionV2()

#Ejemplo 5
#Entradas: 

def clasificacionEdad():
    edad = int(input("Indique su edad: "))
    resultado = " "
    if (edad < 12):
        resultado = "Niño"
    elif (edad >= 12 and edad <= 17):
        resultado = "Adolescente"
    elif (edad >= 18 and edad <=64):
        resultado = "Adulto"
    else:
        resultado = "Adulto Mayor"
    print("Segun su edad se trata de", resultado)
clasificacionEdad()

#Ejemplo 6
#Entradas: precioProducto (float)
#Salida: precioFinal (float)
#Restricciones: precioProducto > 0
def calcularPrecioFinal():
    precioProducto = float(input("Ingrese el valor del producto: "))
    if (precioProducto < 50):
        print("No recibe descuento")
    elif (precioProducto >= 50 and precioProducto < 100):
        precioProducto = precioProducto - (precioProducto * 0.1)
    else:
        precioProducto = precioProducto - (precioProducto * 0.2)
    print("El costo del producto es ", precioProducto)
calcularPrecioFinal()

#Ejemplo 7
#Entradas: ingresosAnuales (float)
#Salida: Impuestos (float)
#Restricciones: ingresoAnual > 0
def calcularImpuestosAnuales():
    ingresoAnual = float(input("Ingrese el monto anual: "))
    if (ingresoAnual < 30000):
        impuestos = ingresoAnual * 0.05
    else:
        if (ingresoAnual >= 30000 and ingresoAnual <= 60000):
            impuestos = ingresoAnual * 0.1
        else: 
            impuestos = ingresoAnual * 0.15
    print("El total de impuestos a pagar es:", impuestos)
calcularImpuestosAnuales()

#Ejemplo 8
#Entradas: peso (float), altura (float)
#Salida: categoria (str)
#Restricciones: peso > 0, altura > 0
def clasificarIMC():
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = peso / altura ** 2
    if (imc < 18.5):
        categoria = "Bajo peso"
    elif (imc >= 18.5 and imc <= 24.9):
        categoria = "Peso normal"
    elif (imc >= 25 and imc <= 29.9):
            categoria = "Sobrepeso"
    else:
        categoria = "Obesidad"
    print("Tu clasificación es ", categoria)
clasificarIMC()

