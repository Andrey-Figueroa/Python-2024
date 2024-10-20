from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import messagebox
from tkinter import Text


def crearFormularioGrafico():
    
    def terminarPrograma(event):
        ventana.destroy()

    ventana = Tk()
    ventana.title("Criptando codigos")
    ventana.eval("tk::PlaceWindow . center")
    ventana.geometry("800x500")
    
    lblOperacionRealizar = Label(text="Operación a realizar:")
    lblAlgoritmo = Label(text="Algoritmo:")
    lblEntrada = Label(text="Entrada:")
    lblSalida = Label(text="Salida:")

    btnAbrirTXT = Button(text="Abrir archivo TXT")
    btnAplicarAlgoritmo = Button(text="Aplicar algoritmo")
    btnSalir = Button(text="SALIR")
    btnEnviarCorreo = Button(text="Enviar por correo")

    entEntrada = Text(ventana, fg="Black", bg="White", height=9, width=90)
    entSalida = Text(ventana, fg="Black", bg="White", height=8, width=90)

    btnSalir.bind("<Button-1>",terminarPrograma)






    lblOperacionRealizar.place(x=35, y=25)
    lblAlgoritmo.place(x=450, y=25)
    lblEntrada.place(x=40, y=70)
    entEntrada.place(x=40, y=90)
    lblSalida.place(x=40, y=290)
    entSalida.place(x=40, y=310)
    btnAplicarAlgoritmo.place(x=350, y=245)
    btnAbrirTXT.place(x=650, y=50)
    btnSalir.place(x=375, y=455)
    btnEnviarCorreo.place(x=650, y=450)

    ventana.mainloop()

crearFormularioGrafico()

