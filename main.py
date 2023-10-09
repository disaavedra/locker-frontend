from data import get_orders, find_mail_by_value
import tkinter as tk
from tkinter import ttk

def click(numero):
    entrada_actual = entrada_var.get()
    if len(entrada_actual) < 8:
        entrada_var.set(entrada_actual + str(numero))

def borrar():
    entrada_var.set("")

def abrir():
    numero_ingresado = entrada_var.get()
    if len(numero_ingresado) == 8:
        orders = get_orders()
        user = find_mail_by_value(orders, int(numero_ingresado))
        if user == None:
            print("Contraseña Incorrecta")
        else:
            print(user)
            print("Número ingresado:", numero_ingresado)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Lockers")

# Variable de control para el widget de entrada
entrada_var = tk.StringVar()

# Crear y posicionar los botones con esquinas redondeadas y padding
style = ttk.Style()
style.configure('TButton', relief="solid", borderwidth=0, bordercolor="gray")
style.map('TButton', background=[('active', 'gray80')])

for i in range(1, 10):
    fila = (i - 1) // 3 + 2  # Calcular la fila en función del número, comenzando desde la fila 2
    columna = (i - 1) % 3     # Calcular la columna en función del número
    texto_boton = str(i)
    boton = ttk.Button(ventana, text=texto_boton, command=lambda num=i: click(num), width=5, style='TButton', padding=(10, 10))
    boton.grid(row=fila, column=columna, padx=10, pady=10)

# Agregar el botón 0 con esquinas redondeadas y padding en la fila 5, columna 1s
boton_0 = ttk.Button(ventana, text="0", command=lambda num=0: click(num), width=5, style='TButton', padding=(10, 10))
boton_0.grid(row=5, column=1, padx=10, pady=10)

# Crear el widget de entrada en la fila 1
entrada = tk.Entry(ventana, textvariable=entrada_var, justify="center", font=("Arial", 18))
entrada.grid(row=1, columnspan=3, padx=10, pady=10)

# Agregar el botón de "Borrar" para limpiar la entrada
boton_borrar = ttk.Button(ventana, text="Borrar", command=borrar, width=20, style='TButton', padding=(10, 10))
boton_borrar.grid(row=6, columnspan=3, padx=10, pady=10)

# Agregar el botón "Abrir" para imprimir el número en consola
boton_abrir = ttk.Button(ventana, text="Abrir", command=abrir, width=20, style='TButton', padding=(10, 10))
boton_abrir.grid(row=7, columnspan=3, padx=10, pady=10)

# Iniciar la aplicación
ventana.mainloop()