import tkinter as tk
from tkinter import messagebox

def calcular_salario():
    try:
        nombre = entry_nombre.get()
        salario_hora = float(entry_salario_hora.get())
        horas_trabajadas = int(entry_horas_trabajadas.get())
        
        salario_mensual = salario_hora * horas_trabajadas
        
        if salario_mensual > 450000:
            resultado = f"Nombre: {nombre}\nSalario Mensual: ${salario_mensual:,.2f}"
        else:
            resultado = f"Nombre: {nombre}\nSalario mensual menor o igual a $450,000."
        
        label_resultado.config(text=resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos en todos los campos.")

root = tk.Tk()
root.title("Cálculo de Salario Mensual")
root.geometry("500x400")

label_nombre = tk.Label(root, text="Nombre del Empleado:")
label_nombre.pack(pady=5)
entry_nombre = tk.Entry(root)
entry_nombre.pack(pady=5)

label_salario_hora = tk.Label(root, text="Salario Básico por Hora:")
label_salario_hora.pack(pady=5)
entry_salario_hora = tk.Entry(root)
entry_salario_hora.pack(pady=5)

label_horas_trabajadas = tk.Label(root, text="Número de Horas Trabajadas:")
label_horas_trabajadas.pack(pady=5)
entry_horas_trabajadas = tk.Entry(root)
entry_horas_trabajadas.pack(pady=5)

btn_calcular = tk.Button(root, text="Calcular Salario", command=calcular_salario)
btn_calcular.pack(pady=10)

label_resultado = tk.Label(root, text="Resultado:", font=("Arial", 12), wraplength=450, justify="left")
label_resultado.pack(pady=10)

root.mainloop()
