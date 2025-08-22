import tkinter as tk

import tkinter as tk
from tkinter import ttk

# Crear ventana principal
root = tk.Tk()
root.title("Calculadora de IMC")
root.geometry("300x250")
root.resizable(False, False)

# Título
titulo = ttk.Label(root, text="Calculadora de IMC", font=("Arial", 14, "bold"))
titulo.pack(pady=10)

# Frame para los campos
frame = ttk.Frame(root, padding=10)
frame.pack(fill="x", expand=True)

# Campo Peso
label_peso = ttk.Label(frame, text="Peso (kg):")
label_peso.grid(row=0, column=0, sticky="w", pady=5)
entry_peso = ttk.Entry(frame)
entry_peso.grid(row=0, column=1, pady=5)

# Campo Altura
label_altura = ttk.Label(frame, text="Altura (m):")
label_altura.grid(row=1, column=0, sticky="w", pady=5)
entry_altura = ttk.Entry(frame)
entry_altura.grid(row=1, column=1, pady=5)

# Botón para calcular
btn_calcular = ttk.Button(root, text="Calcular IMC")
btn_calcular.pack(pady=10)

# Etiqueta para mostrar resultado
label_resultado = ttk.Label(root, text="Resultado: ", font=("Arial", 11))
label_resultado.pack(pady=5)

# Etiqueta para mostrar clasificación
label_clasificacion = ttk.Label(root, text="Clasificación: ", font=("Arial", 11))
label_clasificacion.pack(pady=5)

root.mainloop()
