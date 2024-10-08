#MariangelMonge 2024086680
#Ejemplo de implementacion de una calculadora basica basada en CLI
import logging
import traceback

#configurar el logger
logging.basicConfig(filename="appLogs.log", level=logging.DEBUG, force=True,
                    format='%(asctime)s - %(levelname)s - %(message)s')

#Operaciones basicas de nuestra calculadora

def sumar(a,b):
    return a+b

def restar(a,b): 
    return a-b

def multiplicar(a,b):
    return a*b

#Es una buena practica que las excepciones sean tratadas/manejadas cerca de donde ocurren
#Manejar la excepcion
def dividir(a,b):
    try: 
        return a/b
    except ZeroDivisionError as e: 
        logging.error("Error de division por 0", e.__class__, traceback. format_exception)

#   F, es un float, I es entero
def obtener_numero(mensaje, tipo):
    while (True):
        try:
            if(tipo=="F"):
                return float(input(mensaje))
            if(tipo=="I"):
                return int(input(mensaje))

        except ValueError as e:
            logging.error("Error en la entrada de datos numericos", e)
            logging.error("Traceback:", traceback.format_exc)

        except Exception as e: 
            logging.error("Se presenta una excepcion, verifique", e)
#obtener_numero("Indique un numero: ")

def imprimirMenu():
    print("Calculadora en CLI")
    print("Operaciones>>")
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicacion")
    print("4.Dividir")
    print("5.Para salir...")

def calculadora():
    i=0
    while(True):
        i=i+1
        imprimirMenu()
        operacion= obtener_numero("Indique su opcion:[1...5]","I")
        if(operacion>=1 and operacion<=4):
            num1= obtener_numero("Indique el primer valor: ","F")
            num2= obtener_numero("Indique el segundo valor: ","F")

        if(operacion==1):
            print(sumar(num1, num2))
        elif(operacion==2):
            print(restar(num1, num2))
        elif(operacion==3):
            print(multiplicar(num1, num2))
        elif(operacion==4):
            print(dividir(num1, num2))
        elif(operacion==5):
            print("Saliendo...")
            logging.info("El ciclo se ejecuto", i,"veces")
            break
        else:
            print("La opcion no es valida...")

if(__name__=="__main__"):
    calculadora()