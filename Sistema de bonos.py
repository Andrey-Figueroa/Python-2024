#entradas: Sueldo (int) y antiguedad (int)
s#salidas: Sueldofinal (int)
#restricciones: sueldo > 0 and antiguedad > 0
def sistemasBonosAlEmpleado():
    antiguedad = int(input("Años laborados en la empresa:"))
    sueldo = int(input("Indique el sueldo del empleado: "))
    if (antiguedad > 2 and antiguedad <5):
        bonoAntiguedad = sueldo * 0.2
    elif (antiguedad >= 5):
        bonoAntiguedad = sueldo * 0.3
    else:
        bonoAntiguedad = 0
    #Bono por sueldo
    if (sueldo < 1000):
        bonoSueldo = sueldo * 0.25
    elif (sueldo >=1000 and sueldo <= 3500):
        bonoSueldo = sueldo * 0.15
    else:
        bonoSueldo = sueldo * 0.1
    #Imprimir los resultados 
    if (bonoAntiguedad > bonoSueldo):
        print("Su salario es: ", sueldo + bonoAntiguedad)
        print("Se le aplico bono antiguedad")
    else:
        print("Su salario es: ", sueldo + bonoSueldo)
        print("Se le aplico bono sueldo")
sistemasBonosAlEmpleado()
