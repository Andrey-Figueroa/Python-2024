#Generador de contraseñas
import random
def generarPassword():
    letrasMayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minimoLetraMayusculas = random.randrange(2,3)
    letrasRanMayusculas = random.sample(letrasMayusculas,minimoLetraMayusculas)

    letrasMinisculas = "abcdefghijklmnopqrstuvwyxz"
    minimoLetraMinisculas  = random.randrange(2,3)
    letrasRanMinisculas = random.sample(letrasMinisculas,minimoLetraMinisculas)

    numeros = "0123456789"
    minimoNumeros = random.randrange(2,4)
    numerosRan = random.sample(numeros,minimoNumeros)

    signos = "!@#$%*+"
    cantidadSignos = random.randrange(1,2)
    signosRan = random.sample(signos,cantidadSignos)

    extension = letrasRanMayusculas+letrasRanMinisculas+numerosRan+signosRan
    password = "".join(extension)
    return password

print(generarPassword())