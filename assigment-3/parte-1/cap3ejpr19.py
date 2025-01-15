import tkinter as tk
from tkinter import messagebox
import math

def calcular():
    try:
        lado = float(entry_lado.get())
        if lado <= 0:
            raise ValueError("El lado debe ser un número positivo.")
        
        perimetro = 3 * lado
        altura = (math.sqrt(3) / 2) * lado
        area = (lado * altura) / 2

        label_resultados.config(text=f"Perímetro: {perimetro:.2f}\nAltura: {altura:.2f}\nÁrea: {area:.2f}")
    except ValueError as e:
        messagebox.showerror("Error", f"Entrada no válida: {e}")

root = tk.Tk()
root.title("Cálculo de Triángulo Equilátero")
root.geometry("400x300")

label_lado = tk.Label(root, text="Ingrese el valor del lado:")
label_lado.pack(pady=10)
entry_lado = tk.Entry(root)
entry_lado.pack(pady=10)

btn_calcular = tk.Button(root, text="Calcular", command=calcular)
btn_calcular.pack(pady=10)

label_resultados = tk.Label(root, text="Resultados:\nPerímetro:\nAltura:\nÁrea:", font=("Arial", 12), justify="left")
label_resultados.pack(pady=10)

root.mainloop()
