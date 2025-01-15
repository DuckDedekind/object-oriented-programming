import tkinter as tk
from tkinter import messagebox
import math

def calcular_raices():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a == 0:
            messagebox.showerror("Error", "El valor de A no puede ser 0.")
            return

        discriminante = b**2 - 4*a*c

        if discriminante > 0:
            raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
            raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)
            resultado = f"Raíces reales y diferentes:\nX1 = {raiz1:.2f}\nX2 = {raiz2:.2f}"
        elif discriminante == 0:
            raiz = -b / (2 * a)
            resultado = f"Raíces reales e iguales:\nX = {raiz:.2f}"
        else:
            parte_real = -b / (2 * a)
            parte_imaginaria = math.sqrt(abs(discriminante)) / (2 * a)
            resultado = (
                f"Raíces complejas:\n"
                f"X1 = {parte_real:.2f} + {parte_imaginaria:.2f}i\n"
                f"X2 = {parte_real:.2f} - {parte_imaginaria:.2f}i"
            )

        label_resultado.config(text=resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

root = tk.Tk()
root.title("Ecuación Cuadrática")
root.geometry("500x400")

label_a = tk.Label(root, text="Valor de A:")
label_a.pack(pady=5)
entry_a = tk.Entry(root)
entry_a.pack(pady=5)

label_b = tk.Label(root, text="Valor de B:")
label_b.pack(pady=5)
entry_b = tk.Entry(root)
entry_b.pack(pady=5)

label_c = tk.Label(root, text="Valor de C:")
label_c.pack(pady=5)
entry_c = tk.Entry(root)
entry_c.pack(pady=5)

btn_calcular = tk.Button(root, text="Calcular Raíces", command=calcular_raices)
btn_calcular.pack(pady=10)

label_resultado = tk.Label(root, text="Resultado:", font=("Arial", 12), wraplength=450, justify="left")
label_resultado.pack(pady=10)

root.mainloop()
