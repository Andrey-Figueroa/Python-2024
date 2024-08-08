#capitalize()
#Primera letra de una oracion en mayuscula.
def title():
    string = "el VIAJE eS la RecoMpensa"
    print(F"Antes de title(): {string}")
    string = string.capitalize()
    print(f"Despues de capitalize : {string}")


#f string y capitalize
def nombreApellido():
    Nombre = input("Indique su nombre: ")
    Nombre = Nombre.title()
    Apellido = input("Indique su apellido: ")
    Apellido = Apellido.title()
    print(f"Bienvenido {Nombre}{ Apellido} espero que te encuentres bien.")


#Upper y isupper
def elementoquimico():
    elementoQuimico = input("Indique el elemento quimico que desea saber su masa atomica: ")
    elementoQuimico = elementoQuimico.upper()
    numero = 45.65
    print(F"La masa atomica del elemento {elementoQuimico} es de {numero}")


#lower y islower
def sistemaContable():
    print("\nMenu de opciones")
    print("\n1- Activos")
    print("2- Pasivos")
    print("3- Ingresos")
    print("4- Gastos")
    print("5- Capital social")
    opcion = int(input("Elije tu opcion: "))
    if opcion == 1:
        referencia = input("Indicanos cual es tu activo: ")
        referencia = referencia.lower()
        


#strip remover
def strip():
    nombre = " Andrey "
    print(f"Imprimir {nombre}")
    nombre = " Andrey ".strip(" y")
    print(f"Imprimir {nombre}")

#title and istitle
#Primera letra de una palabra o palabras
def nombreApellidoV2():
    Nombre = input("Indique su nombre: ")
    Nombre = Nombre.title()
    Apellido = input("Indique su apellido: ")
    Apellido = Apellido.title()
    print(f"Bienvenido {Nombre } { Apellido} espero que te encuentres bien.")


#Alineacion en pantalla
#center() argumentos = int  > longitud de la variable /  o (10, "=")
nombre = "Sistema de desicion de inversiones"
nombre = nombre.center(68, "*")
print(f"\n{nombre}")

#ljust
nombre = "Sistema de desicion de inversiones"
nombre = nombre.ljust(68,"=")
print(f"\n{nombre}")

#rjust
nombre = "Sistema de desicion de inversiones"
nombre = nombre.rjust(68,"=")
print(f"\n{nombre}")
