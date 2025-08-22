import tkinter as tk
from tkinter import ttk
from utils.calcular_imc import calcular_imc

def ventana_principal():
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
    btn_calcular = ttk.Button(root, text="Calcular IMC", command=lambda: mostrar_resultado(
        entry_peso.get(),entry_altura.get(), label_resultado, label_clasificacion))
    btn_calcular.pack(pady=10)

    # Etiqueta para mostrar resultado
    label_resultado = ttk.Label(root, text="Resultado: ", font=("Arial", 11))
    label_resultado.pack(pady=5)

    # Etiqueta para mostrar clasificación
    label_clasificacion = ttk.Label(root, text="Clasificación: ", font=("Arial", 11))
    label_clasificacion.pack(pady=5)

    root.mainloop()

def mostrar_resultado(peso, altura, label_resultado, label_clasificacion):
    """Actualiza las etiquetas con el resultado del IMC y su clasificación."""
    imc = calcular_imc(peso, altura)
    label_resultado.config(text=f"Resultado: {imc:.2f}")
    
    if imc < 18.5:
        clasificacion = "Bajo peso"
    elif 18.5 <= imc < 24.9:
        clasificacion = "Peso normal"
    elif 25 <= imc < 29.9:
        clasificacion = "Sobrepeso"
    elif 30 <= imc < 34.9:
        clasificacion = "Obesidad grado 1"
    elif 35 <= imc < 39.9:
        clasificacion = "Obesidad grado 2"
    else:
        clasificacion = "Obesidad grado 3"

    label_clasificacion.config(text=f"Clasificación: {clasificacion}")      