#IMPORTACION DE LIBRERIAS
import tkinter as tk
from tkinter import messagebox

def limpiar_entradas():
    entP.delete(0, tk.END)
    entQ.delete(0, tk.END)
    entIntentos.delete(0, tk.END)
    entNumeroSecreto.delete(0, tk.END)
    entAdivina.delete(0, tk.END)

# Función iniciar del juego
def manejarConversiones():
    try:
        global numeroIntentos, numeroSecreto, intentosRestantes
        
        p = int(entP.get())
        q = int(entQ.get())
        numeroIntentos = int(entIntentos.get())
        
        if p >= q:
            messagebox.showerror("Error", "El valor p debe ser menor que el valor q")
            return

        global numeroSecreto 
        numeroSecreto = int(entNumeroSecreto.get())  # Número ingresado por el usuario
        entNumeroSecreto.config(show='##')

        if not (p <= numeroSecreto <= q):
            messagebox.showerror("Error", "El número secreto debe estar entre p y q.")
            return
        
        intentosRestantes = numeroIntentos
        resultado.config(text=f"Te quedan {numeroIntentos} intentos.")
        entAdivina.config(state='normal')  # Cambiar 'Normal' a 'normal'
        btnAdivina.config(state='normal')   # Cambiar 'Normal' a 'normal'

    except ValueError:
        messagebox.showerror("Error", "Ingresar valores numéricos válidos.")

# Verificar número
def verificarNumero():
    global intentosRestantes
    try:
        adivinanza = int(entAdivina.get())
        intentosRestantes -= 1

        if adivinanza == numeroSecreto:
            resultado.config(text="¡Felicidades! Adivinaste el número.")
            entAdivina.config(state='disabled')
            btnAdivina.config(state='disabled')
        elif adivinanza < numeroSecreto:
            resultado.config(text=f"El número es mayor. Quedan {intentosRestantes} intentos.")
        else:
            resultado.config(text=f"El número es menor. Quedan {intentosRestantes} intentos.")
        
        if intentosRestantes == 0 and adivinanza != numeroSecreto:
            resultado.config(text=f"Perdiste. El número era {numeroSecreto}.")
            entAdivina.config(state='disabled')
            btnAdivina.config(state='disabled')

    except ValueError:
        messagebox.showerror("Error", "Ingresar un número válido.")

# Reinicio de juego
def reinicioJuego():
    limpiar_entradas()
    entP.delete(0, tk.END)
    entQ.delete(0, tk.END)
    entNumeroSecreto.delete(0, tk.END)
    entIntentos.delete(0, tk.END)
    entAdivina.delete(0, tk.END)
    entAdivina.config(state='disabled')
    btnAdivina.config(state='disabled')
    resultado.config(text="")

# Cerrar juego
def cerrarVentana():
    ventana.quit()

# Ventana principal
ventana = tk.Tk()
ventana.title("Juego Adivinar el Número")
ventana.geometry("800x400")  # Ajustamos el tamaño de la ventana

# Etiquetas y entradas para valores p y q
tk.Label(ventana, text="Bienvenido al Juego", font=("Arial", 16)).place(x=320, y=20)

tk.Label(ventana, text="Valor mínimo:", font=("Arial", 12), fg="purple").place(x=100, y=80)
entP = tk.Entry(ventana, width=10)
entP.place(x=220, y=80)

tk.Label(ventana, text="Valor máximo:", font=("Arial", 12), fg="purple").place(x=500, y=80)
entQ = tk.Entry(ventana, width=10)
entQ.place(x=620, y=80)

tk.Label(ventana, text="Cantidad de intentos:", font=("Arial", 12), fg="purple").place(x=100, y=160)
entIntentos = tk.Entry(ventana, width=10)
entIntentos.place(x=270, y=160)

# Etiqueta para mostrar el número secreto (invisible al jugador)
tk.Label(ventana, text="Número secreto:", font=("Arial", 12), fg="blue").place(x=100, y=240)
entNumeroSecreto = tk.Entry(ventana, width=10)
entNumeroSecreto.place(x=250, y=240)

# Etiqueta para mostrar resultados
resultado = tk.Label(ventana, text="", font=("Arial", 12), fg="black")
resultado.place(x=100, y=300)

# Botón para iniciar el juego
btnIniciar = tk.Button(ventana, text="Empezar...", font=("Arial", 10), command=manejarConversiones)
btnIniciar.place(x=320, y=200)

# Etiquetas y entradas para adivinanza
tk.Label(ventana, text="Adivinanza:", font=("Arial", 12), fg="blue").place(x=500, y=240)
entAdivina = tk.Entry(ventana, width=10, state='disabled')
entAdivina.place(x=620, y=240)

# Botón para adivinar
btnAdivina = tk.Button(ventana, text="Adivinar", command=verificarNumero, state='disabled')
btnAdivina.place(x=400, y=280)

# Botón salir
btnSalir = tk.Button(ventana, text="Salir", command=cerrarVentana, bg="red", fg="white")
btnSalir.place(x=10, y=350)


btnReiniciar = tk.Button(ventana, text="Reiniciemos", command=reinicioJuego,bg="green", fg="white")
btnReiniciar.place(x=500, y=350, width=100, height=30)

# Ejecutar la ventana principal
ventana.mainloop()