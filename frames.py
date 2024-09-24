import tkinter as tk
ventana = tk.Tk()

ventana.title("Mi ventana")
ventana.geometry("600x400")
ventana.configure(bg="lightblue")
ventana.iconbitmap("luz.ico")
ventana.attributes("-alpha", 0.9)

labelframe = tk.LabelFrame(ventana, text="Grupo de Widgets", bg="yellow", padx=10, pady=10)
labelframe.configure(width=300, height=200)
labelframe.pack()

"""frame1 = tk.Frame(ventana)
frame1.configure(width=300, height=200, bg="red", bd=5)
frame1.pack()

frame2 = tk.Frame(frame1)
frame2.configure(width=100, height=100, bg="blue", bd=5)


boton = tk.Button(frame1, text="Hola")
boton.pack()
frame2.pack()"""

ventana.mainloop()