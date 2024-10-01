import tkinter as tk
from tkinter import messagebox

def delete_last_character():
    text_length = len(display.get())
    if text_length >= 1:
        display.delete(text_length - 1, tk.END)
    if text_length == 1:
        replace_text("0")

def replace_text(text):
    display.delete(0, tk.END)
    display.insert(0, text)

def append(text):
    actual_text = display.get()
    if actual_text == "0":
        replace_text(text)
    else:
        display.insert(tk.END, text)

def evaluate():
    try:
        result = eval(display.get())
        replace_text(result)
    except (SyntaxError, AttributeError):
        messagebox.showerror("Error", "Syntax Error")
        replace_text("0")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Syntax Error")
        replace_text("0")

def change_sign():
    actual_text = display.get()
    if actual_text.startswith('-'):
        replace_text(actual_text[1:])
    else:
        replace_text('-' + actual_text)

def inverse():
    display.insert(0, "1/(")
    append(")")
    evaluate()

# Crear la ventana principal
Calculator = tk.Tk()
Calculator.title("Calculadora simple")
Calculator.resizable(False, False)
Calculator.config(bg="#f0f0f0")

# Crear el campo de entrada
display = tk.Entry(Calculator, font=("Arial", 24), justify='right', bg='azure', fg='black')
display.insert(0, "0")
display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

# Crear botones
buttons = [
    ('CE', delete_last_character, 'blue'),
    ('1/x', inverse, 'gold'),
    ('Del', delete_last_character, 'red'),
    ('/', lambda: append('/'), 'slateblue2'),
    ('7', lambda: append('7'), 'lightgrey'),
    ('8', lambda: append('8'), 'lightgrey'),
    ('9', lambda: append('9'), 'lightgrey'),
    ('*', lambda: append('*'), 'royalblue1'),
    ('4', lambda: append('4'), 'lightgrey'),
    ('5', lambda: append('5'), 'lightgrey'),
    ('6', lambda: append('6'), 'lightgrey'),
    ('-', lambda: append('-'), 'deepskyblue2'),
    ('1', lambda: append('1'), 'lightgrey'),
    ('2', lambda: append('2'), 'lightgrey'),
    ('3', lambda: append('3'), 'lightgrey'),
    ('+', lambda: append('+'), 'dodgerblue2'),  # Cambia a evaluate al pulsar '='
    ('+/-', change_sign, 'blueviolet'),
    ('0', lambda: append('0'), 'lightgrey'),
    ('.', lambda: append('.'), 'lightgrey'),
    ('=', evaluate, 'seagreen1')
]

row_val = 1
col_val = 0

for (text, command, color) in buttons:
    button = tk.Button(Calculator, text=text, command=command, bg=color, fg='black', font=("Arial", 14))
    
    button.grid(row=row_val, column=col_val, sticky="nsew", padx=5, pady=5)
    col_val += 1
    
    # Reiniciar la columna y aumentar la fila si es necesario
    if col_val > 3:
        col_val = 0
        row_val += 1

# Ajustar el tamaño de las filas y columnas
for i in range(4):
    Calculator.grid_columnconfigure(i, weight=1)
for i in range(6):
    Calculator.grid_rowconfigure(i, weight=1)

# Iniciar el bucle principal
Calculator.mainloop()
