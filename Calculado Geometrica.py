#Calculadora geometrica
def rectangulo():
    print("Opciones:\n1-Perimetro del rectangulo\n2-Area del rectangulo")
    opcionRectangulo = int(input("Cual opcion deseas: "))
    baseRectangulo = float(input("Cuanto mide la base: "))
    alturaRectangulo = float(input("Cuanto mide la altura: "))
    if opcionRectangulo == 1:
        operacion = "Perimetro"
        resultado = 2 * (baseRectangulo + alturaRectangulo)
    elif opcionRectangulo == 2:
        operacion = "Area"
        resultado = baseRectangulo * alturaRectangulo
    else:
        print("La opcion no existe.")
    print(f"El {operacion} del rectangulo es de: {resultado}")
#rectangulo()
def triangulo():
    import math
    print("Opciones:\n1-Perimetro del triangulo\n2-Area del triangulo")
    opcionTriangulo = int(input("Cual opcion deseas: "))
    medida1 = float(input("Cuanto mide el primer lado: "))
    medida2 = float(input("Cuanto mide el segundo lado: "))
    medida3 = float(input("Cuanto mide el tercer lado: "))
    if opcionTriangulo == 1:
        operacion = "Perimetro"
        resultado = medida1 + medida2 + medida3
    elif opcionTriangulo == 2:
        operacion = "Area"
        sp = ((medida1 + medida2 + medida3)/2)
        resultado = math.sqrt(sp * (sp - medida1) * (sp - medida2) * (sp - medida3))
    else:
        print("La opcion no existe")
    print(f"El {operacion} del rectangulo es de: {resultado}")
#triangulo()
def distanciaPuntos():
    import math
    print("Calcular distancia entre puntos")
    x1 = float(input("Indique cual es tu x1: "))
    y1 = float(input("Indique cual es tu y1: "))
    x2 = float(input("Indique cual es tu x2: "))
    y2 = float(input("Indique cual es tu y2: "))
    distancia = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    print(f"La distancia entre los puntos es de {distancia:.2f}.")
#distanciaPuntos()
def circulo():
    import math
    print("Opciones:\n1-Area de la esfera\n2-Volumen de la esfera")
    opcionCirculo = int(input("Cual opcion deseas: "))
    radioDiametro = input("Con que deseas realizar tu ejercicio (diametro o radio): ")

    if radioDiametro.lower() == "diametro":
        diametro = float(input("Cuanto mide el diametro: "))
        radio = diametro / 2
    elif radioDiametro.lower() == "radio":
        radio = float(input("Cuanto mide el radio: "))
    else:
        print("La opcion no existe")
    if opcionCirculo == 1:
        operacion = "Area"
        resultado = math.pi * 4 * radio**2
    elif opcionCirculo == 2:
        operacion = "Volumen"
        resultado = 1/3 * math.pi * radio**3
    else:
        print("La opcion no existe")
    print(f"El {operacion} de la esfera es de: {resultado:.2f}.")
circulo()
