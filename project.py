import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Conversor de temperatura")
ventana.config(width=400, height=300, bg='lightblue')

def convertir_temp():
    temp_celsius = float(caja_temp_celsius.get())
    temp_kelvin = temp_celsius + 273.15
    temp_fahrenheit = temp_celsius * 1.8 + 32
    etiqueta_temp_kelvin.config(text="Temperatura en K: {:.2f}".format(temp_kelvin))
    etiqueta_temp_fahrenheit.config(text="Temperatura en F: {:.2f}".format(temp_fahrenheit))

# Etiqueta para la entrada de temperatura en Celsius
etiqueta_temp_celsius = ttk.Label(ventana, text="Temperatura en grados Celsius", font=('Arial', 10, 'bold'), background='lightblue')
etiqueta_temp_celsius.place(x=100, y=20)

# Entrada para la temperatura en Celsius
caja_temp_celsius = ttk.Entry(ventana)
caja_temp_celsius.place(x=150, y=50, width=60)

# Etiqueta para la temperatura en Kelvin
etiqueta_temp_kelvin = ttk.Label(ventana, text="Temperatura en K: n/a", font=('Arial', 10, 'bold'), background='lightblue')
etiqueta_temp_kelvin.place(x=20, y=120)

# Etiqueta para la temperatura en Fahrenheit
etiqueta_temp_fahrenheit = ttk.Label(ventana, text="Temperatura en F: n/a", font=('Arial', 10, 'bold'), background='lightblue')
etiqueta_temp_fahrenheit.place(x=20, y=160)

# Botón para convertir la temperatura
boton_convertir = ttk.Button(ventana, text="Convertir", command=convertir_temp)
boton_convertir.place(x=150, y=90)
boton_convertir.config(style='TButton')

# Configurar el estilo del botón
style = ttk.Style()
style.configure('TButton', background='gray', font=('Arial', 10, 'bold'))


# Ejecutar el bucle principal
ventana.mainloop()
