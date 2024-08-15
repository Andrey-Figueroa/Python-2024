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
 