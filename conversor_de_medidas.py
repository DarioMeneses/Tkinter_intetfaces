import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Conversor de Medidas")
ventana.config(bg="#A8E6CE")  # Fondo verde claro
ventana.geometry("400x400")

def convertir_medidas():
    try:
        valor = float(caja_valor.get())
        unidad_origen = combo_unidades.get()

        # Inicializar conversiones
        mm = m = cm = km = 0.0

        # Realizar conversiones según la unidad seleccionada
        if unidad_origen == "Kilómetros":
            mm = valor * 1_000_000
            m = valor * 1_000
            cm = valor * 100
            km = valor
        elif unidad_origen == "Metros":
            mm = valor * 1_000
            km = valor / 1_000
            cm = valor * 100
            m = valor
        elif unidad_origen == "Centímetros":
            mm = valor * 10
            km = valor / 100_000
            m = valor / 100
            cm = valor
        elif unidad_origen == "Milímetros":
            km = valor / 1_000_000
            m = valor / 1_000
            cm = valor / 10
            mm = valor

        # Mostrar resultados
        etiqueta_resultado.config(text=f"Conversión de {valor} {unidad_origen}:\n"
                                         f"{mm:.2f} mm\n"
                                         f"{m:.2f} m\n"
                                         f"{cm:.2f} cm\n"
                                         f"{km:.6f} km", font=("Arial", 12, "bold"))
    except ValueError:
        etiqueta_resultado.config(text="Ingrese un número válido", font=("Arial", 12, "bold"))

# Etiqueta de entrada
etiqueta_valor = ttk.Label(ventana, text="Valor:", background="#A8E6CE", font=("Arial", 12, "bold"))
etiqueta_valor.pack(pady=10)

# Caja de entrada
caja_valor = ttk.Entry(ventana, font=("Arial", 12))
caja_valor.pack(pady=10)

# Selección de unidades
etiqueta_unidades = ttk.Label(ventana, text="Unidad de origen:", background="#A8E6CE", font=("Arial", 12, "bold"))
etiqueta_unidades.pack(pady=10)

combo_unidades = ttk.Combobox(ventana, values=["Kilómetros", "Metros", "Centímetros", "Milímetros"], state="readonly", font=("Arial", 12))
combo_unidades.pack(pady=10)
combo_unidades.current(0)  # Seleccionar por defecto "Kilómetros"

# Botón de conversión
boton_convertir = ttk.Button(ventana, text="Convertir", command=convertir_medidas)
boton_convertir.pack(pady=10)
boton_convertir.config(style="TButton")

# Etiqueta para mostrar el resultado
etiqueta_resultado = ttk.Label(ventana, text="", background="#A8E6CE", font=("Arial", 12, "bold"))
etiqueta_resultado.pack(pady=20)

# Estilo para el botón
style = ttk.Style()
style.configure("TButton", background="#2E7D32", foreground="black", font=("Arial", 12, "bold"))
style.map("TButton", background=[("active", "#1B5E20")])

# Iniciar el bucle principal
ventana.mainloop()
