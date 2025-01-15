import tkinter as tk
from tkinter import messagebox

def comparar():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        
        if a > b:
            resultado = "A es mayor que B"
        elif a == b:
            resultado = "A es igual a B"
        else:
            resultado = "A es menor que B"

        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

root = tk.Tk()
root.title("Comparar A y B")
root.geometry("400x300")

label_a = tk.Label(root, text="Ingrese el valor de A:")
label_a.pack(pady=10)
entry_a = tk.Entry(root)
entry_a.pack(pady=5)

label_b = tk.Label(root, text="Ingrese el valor de B:")
label_b.pack(pady=10)
entry_b = tk.Entry(root)
entry_b.pack(pady=5)

btn_comparar = tk.Button(root, text="Comparar", command=comparar)
btn_comparar.pack(pady=10)

label_resultado = tk.Label(root, text="Resultado: ", font=("Arial", 12))
label_resultado.pack(pady=10)

root.mainloop()
