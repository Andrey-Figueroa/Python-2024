def sistemasDeducciones():
    sistema = " Sistema de deducciones salariales "
    sistema = sistema.center(100,"*")
    print(f"{sistema}\n")
    salario = int(input("Indique su salario: "))
    monto1, monto2, monto3, monto4 = 929000, 1363000, 2392000, 4783000
    if (salario <= monto1):
        salario = salario - (salario*0.1067)
        print(f"\nImpuesto de la CCSS son de: {ccss}")
        print(f"Sus impuestos de renta son de: {(sobrecargo + impuestos)}")
        print(f"Su salario neto es de: {salario}")
    elif (salario > monto1 and salario <= monto2):
        salario = (salario-(salario - monto1)*0.1)-(salario*0.1067)
        print(f"\nImpuesto de la CCSS son de: {ccss}")
        print(f"Sus impuestos de renta son de: {(sobrecargo + impuestos)}")
        print(f"Su salario neto es de: {salario}")
    elif (salario > monto2 and salario <= monto3):
        sobrecargo = (monto2 - monto1 )* 0.1
        ccss = (salario*0.1067)
        impuestos = (salario - monto2) *0.15
        salario = salario - (sobrecargo + impuestos+ccss)
        print(f"\nImpuesto de la CCSS son de: {ccss}")
        print(f"Sus impuestos de renta son de: {(sobrecargo + impuestos)}")
        print(f"Su salario neto es de: {salario}")
    elif (salario > monto3 and salario <= monto4):
        sobrecargo = ((monto2 - monto1 )* 0.1) + ((monto3-monto2)*0.15)
        ccss = (salario*0.1067)
        impuestos = (salario - monto3) *0.2
        salario = salario - (sobrecargo + impuestos+ccss)
        print(f"\nImpuesto de la CCSS son de: {ccss}")
        print(f"Sus impuestos de renta son de: {(sobrecargo + impuestos)}")
        print(f"Su salario neto es de: {salario}")
    else:
        sobrecargo = ((monto2 - monto1 )* 0.1) + ((monto3-monto2)*0.15) + ((monto4-monto3)*0.2)
        ccss = (salario*0.1067)
        impuestos = (salario - monto4) *0.25
        salario = salario - (sobrecargo + impuestos+ccss)
        print(f"\nImpuesto de la CCSS son de: {ccss}")
        print(f"Sus impuestos de renta son de: {(sobrecargo + impuestos)}")
        print(f"Su salario neto es de: {salario}")

sistemasDeducciones()