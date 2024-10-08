#Andrey Figueroa 2024091038
import logging
import traceback

# Configurar el logger
logging.basicConfig(filename='appLogs.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Operaciones básicas de nuestra calculadora
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

# Manejar la excepción de división por cero
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        logging.error(f"Error por división por 0: {e.__class__.__name__}\n{traceback.format_exc()}")
        return "Error: No se puede dividir por cero"

# Función para obtener número con manejo de excepciones
def obtener_numero(mensaje, tipo):
    while(True):
        try:
            if tipo == "F":
                return float(input(mensaje))
            if tipo == "I":
                return int(input(mensaje))
        except ValueError as e:
            logging.error(f"Error en la entrada de datos numéricos: {e.__class__.__name__}\n{traceback.format_exc()}")
            print("Entrada inválida, intente de nuevo.")
        except Exception as e:
            logging.error(f"Se presentó una excepción: {e.__class__.__name__}\n{traceback.format_exc()}")
            print("Ocurrió un error, intente de nuevo.")

# Función para imprimir el menú de la calculadora
def imprimirMenu():
    print("Calculadora en CLI")
    print("Operaciones >>")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

# Función principal de la calculadora
def calculadora():
    while(True):
        imprimirMenu()
        operacion = obtener_numero("Indique su opción: [1...5] ", "I")

        if operacion == 5:
            print("Saliendo...")
            break

        if operacion >= 1 and operacion <= 4:
            num1 = obtener_numero("Indique el primer valor: ", "F")
            num2 = obtener_numero("Indique el segundo valor: ", "F")

            if operacion == 1:
                print(f"Resultado: {sumar(num1, num2)}")
            elif operacion == 2:
                print(f"Resultado: {restar(num1, num2)}")
            elif operacion == 3:
                print(f"Resultado: {multiplicar(num1, num2)}")
            elif operacion == 4:
                print(f"Resultado: {dividir(num1, num2)}")
        else:
            print("La opción no es válida...")

if __name__ == "__main__":
    calculadora()