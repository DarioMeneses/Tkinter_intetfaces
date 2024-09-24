# tkinter interfaces
import tkinter as tk

ventana = tk.Tk()

ventana.title("Mi primera ventana")

ventana.geometry("600x400+0+0") # Cambia las dimensiones de la ventana

ventana.minsize(400, 200) # Configura la ventana para que no se pueda minimizar desde ciertos parametros

ventana.maxsize(800, 600) # Configura la ventana a un tamaño maximo

ventana.iconbitmap("luz.ico")

ventana.configure(bg="lightblue")

ventana.resizable(False, True)

ventana.attributes("-alpha", 0.9)

ventana.mainloop()