#"Bienvenidos al sistema de consultas salariales" 
print("Bienvenidos al sistema de consultas salariales".center(92))
nombreUsuario = input("Con quien tengo el gusto: ")
print(f"Hola, {nombreUsuario.capitalize()} te presento el menu de opciones: \n")
print("1- Calculo de deducciones salariales\n2- Calculo de liquidacion al empleado\n")
opcionElegida = int(input("Cual opcion deseas utilizar: "))
if opcionElegida == 1:
    def deduccionesSalariales():
        print("Calculemos tus deducciones".center(100))
        moneda = input("¿Ganas en dolares o colones?: ")
        moneda = moneda.lower()
        salarioBruto = float(input("Indica tu salario bruto: "))
        if moneda == "dolares" or "usd":
            salarioBruto = salarioBruto * 526.32
        asociacionSolidarista = input("¿Perteneces a la asociacion solidarista? responde si o no: ")
        asociacionSolidarista = asociacionSolidarista.lower()
    #Caso 1
        if salarioBruto <= 929000:
            impuestos = 0
            impuestoTotal = 0
            ccss = salarioBruto * 0.1067
            if asociacionSolidarista == "si":
                asociacionSolidarista = salarioBruto * 0.05
            else:
                asociacionSolidarista = salarioBruto * 0
            salarioNeto = salarioBruto - impuestos - ccss - asociacionSolidarista
    #Caso 2
        elif salarioBruto > 929000 and salarioBruto <= 1363000:
            impuestos = (salarioBruto - 929000) * 0.1
            impuestoTotal = impuestos
            ccss = salarioBruto * 0.1067
            if asociacionSolidarista == "si":
                asociacionSolidarista = salarioBruto * 0.05
            else:
                asociacionSolidarista = salarioBruto * 0
            salarioNeto = salarioBruto - impuestos - ccss - asociacionSolidarista
    #Caso 3
        elif salarioBruto > 1363000 and salarioBruto <= 2392000:
            impuestos = (salarioBruto - 1363000)*0.15
            sobrecargo1 = (1363000- 929000)*0.1
            impuestoTotal = impuestos + sobrecargo1
            ccss = salarioBruto * 0.1067
            if asociacionSolidarista == "si":
                asociacionSolidarista = salarioBruto * 0.05
            else:
                asociacionSolidarista = salarioBruto * 0
            salarioNeto = salarioBruto - impuestoTotal - asociacionSolidarista - ccss
    #Caso 4
        elif (salarioBruto > 2392000 and salarioBruto <= 4783000):
            impuestos = (salarioBruto - 2392000) * 0.20
            sobrecargo1 = (1363000 - 929000) * 0.1
            sobrecargo2 = (2392000 - 1363000)* 0.15
            impuestoTotal = impuestos + sobrecargo1 + sobrecargo2
            ccss = salarioBruto * 0.1067
            if asociacionSolidarista == "si":
                asociacionSolidarista = salarioBruto * 0.05
            else:
                asociacionSolidarista = salarioBruto * 0
            salarioNeto = salarioBruto - impuestoTotal - asociacionSolidarista - ccss             
    #Caso 5
        else:
            impuestos = (salarioBruto - 4783000) * 0.25
            sobrecargo1, sobrecargo2, sobrecargo3 = (1363000 - 929000) * 0.1, (2392000 - 1363000)* 0.15, (4783000 - 2392000) * 0.20
            impuestoTotal = impuestos + sobrecargo1 + sobrecargo2 + sobrecargo3
            ccss = salarioBruto * 0.1067
            if asociacionSolidarista == "si":
                asociacionSolidarista = salarioBruto * 0.05
            else:
                asociacionSolidarista = salarioBruto * 0
            salarioNeto = salarioBruto - impuestoTotal - asociacionSolidarista - ccss
        print(f"Listo {nombreUsuario.capitalize()} hemos calculado tus deducciones salariales, son:")
        print(f"\nImpuesto sobre la renta: \t₡{impuestoTotal:.2f}")
        print(f"Deducciones de la Caja del Seguro Costarricense = \t₡{ccss:.2f}")
        if asociacionSolidarista > 0:
            print(f"Su aporte a la asocción solidarista es de: \t₡{asociacionSolidarista:.2f}")
        else:
            print("No cuentas con aportes a la asociación solidarista.")
        print(f"Tu salario Neto sera de: \t₡{salarioNeto:.2f}")
    deduccionesSalariales()
elif opcionElegida == 2:
    
else:
    print("Opcion no encontrada")


