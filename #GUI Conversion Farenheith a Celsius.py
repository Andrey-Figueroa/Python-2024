#Importacion de librerias
from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import messagebox

#FUNCION NEUTRAL a la INTERFAZ
def convertirFarenheithACelsius(gradosFarenheith):
    return(gradosFarenheith - 32) / 1.8

#USANDO CLI
def programa():
    print("Indique la cantidad de grados Farenheit: ")
    while(True):
        try:
            gradosFarenheith = float(input())
            break
        except:
            print("Por favor indicar un valor numerico")
    if(gradosFarenheith >= -150 and gradosFarenheith <= 150):
        print("El resultado de la conversíon a Celsius es: ", convertirFarenheithACelsius(gradosFarenheith))
    else:
        print("El valor indicado no esta en un rango aceptable")
print(programa())


def crearFormularioGrafico():

    def terminarPrograma(event):
        ventana.destroy()
    
    def manejarConversion(event):
        try:
            valor = float(entGradosFareheith.get())
            if(valor >-150 and valor <= 150):
                entGradosCelsius.insert(0,convertirFarenheithACelsius(valor))
            else:
                messagebox.showinfo(message= "Debe indicar un valor numerico entre -150 y 150",title = "AVISO")
        except:
            messagebox.showinfo(message="Debe indicar un valor numerico",title = "AVISO")


#USANDO GUI
    #Elementos graficos a utilizar / widgets
    ventana = Tk()
    #Cambiar titulo de la ventana
    ventana.title("Temperatura Converter")
    #Posicionar la ventana en el centro de la pantalla
    ventana.eval("tk::PlaceWindow . center")
    #Definir tamaño de la ventana en pixeles
    ventana.geometry("500x250")

    #Creacion de etiquetas -- equivalente a prints en consola
    lblGradosFarenheith = Label(text="Indique la cantidad de grados farenheith:")
    #Creacion de elementos para entradas de datos -- equivalentes
    entGradosFareheith = Entry(fg="Yellow", bg="Blue",width=10)
    entGradosCelsius = Entry(fg="Yellow", bg="Blue",width=10) #ancho
    #Creacion de etiquetas --- equivalente a prints en consola
    lblGradosCelsius = Label(text="El resultado de la conversion es:")
    #Creacion de un boton -- que realice alguna accion al servidor
    btnConvertir = Button(text="Convertir...")
    #Creacion de un boton -- para permitir cerrar la ventana
    btnSalir = Button(text="Salir >")

    #Relacionar los botones (bind = relacionar)con el click izquierdo y derecho y una accion
    btnConvertir.bind("<Button-1>",manejarConversion)
    btnConvertir.bind("<Return>",manejarConversion)
    btnSalir.bind("<Button-1>",terminarPrograma)

    #Colocar los componentes graficos al objetivo ventana
    lblGradosFarenheith.place(x=40, y=25)
    entGradosFareheith.place(x=315,y=22)
    lblGradosCelsius.place(x=40, y=25)
    entGradosCelsius.place(x=315,y=140)
    btnConvertir.place(x=220, y=85)
    btnSalir.place(x=440, y=220)

    #Inicia el monitoreo de eventos indefinidamente
    ventana.mainloop()

crearFormularioGrafico()
