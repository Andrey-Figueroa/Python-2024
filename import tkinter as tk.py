#Andrey Gustavo Figueroa Calderon 2024091038
#Laboratorio TKINTER ADIVINA EL JUEGO
#Le querido incluir a el programa y la interfaz que los participantes coloquen sus nombres, para desafiarme y que sea mas interactivo

import tkinter as tk
from tkinter import messagebox


def limpiar_entradas():
    entAdivinador.delete(0, tk.END)
    entGenerador.delete(0, tk.END)
    entMaximo.delete(0, tk.END)
    entMinimo.delete(0, tk.END)
    entIntentos.delete(0, tk.END)
    entNumeroSecreto.delete(0, tk.END)
    entAdivinanza.delete(0, tk.END)
    entIntentosRestantes.delete(0, tk.END)

# Función para inicializar el juego
def manejarConversiones():
    try:
        maximo = int(entMaximo.get())
        minimo = int(entMinimo.get())
        intentos = int(entIntentos.get())
        
        adivinador = entAdivinador.get()
        generador = entGenerador.get()
        
        if (adivinador == "" or generador == ""):
            messagebox.showerror(message="Cuidado, uno de los nombres está vacío", title="AVISO")
            return
        
        # Corregido: maximo debe ser mayor que minimo
        if maximo <= minimo or intentos <= 0:
            messagebox.showerror(message="Revisen los números que han dado como máximo, mínimo e intentos", title="AVISO")
            return
        
        # Solicitar a P2 que ingrese el número secreto
        global numeroSecreto 
        numeroSecreto = int(entNumeroSecreto.get())
        entNumeroSecreto.config(show='*')
        
        # Corregido: el número secreto debe estar entre minimo y maximo
        if numeroSecreto < minimo or numeroSecreto > maximo:
            messagebox.showinfo(message=f"{generador}, revisa el número secreto, debe estar dentro del rango ({minimo} - {maximo}).", title="AVISO")
            return
        
        # Actualizar estado de la interfaz
        lblInfo.config(text=f"{adivinador}, adivina un número entre {minimo} y {maximo}")
        entAdivinanza.config(state='normal')
        btnAdivinar.config(state='normal')
        entIntentosRestantes.config(state='normal')
        global intentosRestantes
        intentosRestantes = intentos
        entIntentosRestantes.delete(0, tk.END)
        entIntentosRestantes.insert(0, str(intentosRestantes))
        
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números válidos.")

# Función para manejar la adivinanza
def adivinar():
    try:
        global intentosRestantes
        adivinador = entAdivinador.get()
        generador = entGenerador.get()
        intento = int(entAdivinanza.get())
        
        if intentosRestantes > 0:
            if intento == numeroSecreto:
                messagebox.showinfo("¡Felicidades!", f"{adivinador}, has adivinado el número. ¡Ganaste!")
                reiniciar_juego()
            elif intento < numeroSecreto:
                messagebox.showinfo("Pista", f"{adivinador}, el número es mayor.")
                intentosRestantes -= 1
                entIntentosRestantes.delete(0, tk.END)
                entIntentosRestantes.insert(0, str(intentosRestantes))
            else:
                messagebox.showinfo("Pista", f"{adivinador}, el número es menor.")
                intentosRestantes -= 1
                entIntentosRestantes.delete(0, tk.END)
                entIntentosRestantes.insert(0, str(intentosRestantes))
            
            if intentosRestantes == 0:
                messagebox.showinfo("Fin del juego", f"{adivinador}, te has quedado sin intentos. El número era {numeroSecreto}. {generador} gana.")
                reiniciar_juego()
                
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un número válido.")

# Función para reiniciar el juego
def reiniciar_juego():
    limpiar_entradas()
    entMaximo.config(state='normal')
    entMinimo.config(state='normal')
    entIntentos.config(state='normal')
    entNumeroSecreto.config(state='normal')
    entAdivinanza.config(state='disabled')
    btnAdivinar.config(state='disabled')
    entIntentosRestantes.config(state='disabled')
    lblInfo.config(text="Configura el juego e inicia")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Adivina el Número")
ventana.eval("tk::PlaceWindow . center")
ventana.geometry("900x500")

# Widgets para ingresar los nombres de los jugadores
tk.Label(ventana, text="¿Quién quiere adivinar? (Digita tu nombre):").place(x=100, y=60)
entAdivinador = tk.Entry(ventana)
entAdivinador.place(x=100, y=90, width=250, height=30)

tk.Label(ventana, text="¿Quién quiere escoger el número? (Digita tu nombre):").place(x=550, y=60)
entGenerador = tk.Entry(ventana)
entGenerador.place(x=550, y=90, width=250, height=30)

# Elementos de la interfaz para definir el rango y los intentos
lblTitulo = tk.Label(ventana, text="BIENVENIDO AL JUEGO", font=("Arial", 16))
btnSalir = tk.Button(ventana, text="SALIR >>>", command=ventana.quit)
tk.Label(ventana, text="Valor mínimo: ").place(x=100, y=150)
entMinimo = tk.Entry(ventana)
entMinimo.place(x=200, y=150, width=150, height=30)

tk.Label(ventana, text="Valor máximo: ").place(x=100, y=190)
entMaximo = tk.Entry(ventana)
entMaximo.place(x=200, y=190, width=150, height=30)

tk.Label(ventana, text="Número de intentos:").place(x=100, y=230)
entIntentos = tk.Entry(ventana)
entIntentos.place(x=250, y=230, width=150, height=30)

tk.Label(ventana, text="Número secreto: ").place(x=100, y=280)
entNumeroSecreto = tk.Entry(ventana)
entNumeroSecreto.place(x=250, y=280, width=200, height=30)

btnIniciar = tk.Button(ventana, text="Iniciar juego", command=manejarConversiones)
btnIniciar.place(x=375, y=90, width=125, height=30)

lblInfo = tk.Label(ventana, text="Rellena los valores y empecemos.....")
lblInfo.place(x=350, y=330)

# Elementos de la interfaz para las adivinanzas
tk.Label(ventana, text="Número adivinanza (P1):").place(x=100, y=420)
entAdivinanza = tk.Entry(ventana, state='disabled')
entAdivinanza.place(x=250, y=420, width=200, height=30)

btnAdivinar = tk.Button(ventana, text="Adivinar", state='disabled', command=adivinar)
btnAdivinar.place(x=600, y=330)

tk.Label(ventana, text="Intentos restantes:").place(x=100, y=370)
entIntentosRestantes = tk.Entry(ventana, state='disabled')
entIntentosRestantes.place(x=250, y=370, width=200, height=30)
btnSalir.place(x=750, y=450, width=100, height=30)
lblTitulo.place(x=350, y=20)

# Iniciar loop de la ventana
ventana.mainloop()
