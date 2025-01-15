import tkinter as tk
from tkinter import messagebox

def calcular_matricula():
    try:
        ni = entry_ni.get()
        nom = entry_nom.get()
        pat = float(entry_pat.get())
        es = int(entry_es.get())
        
        pagmat = 50000
        
        if pat > 2000000 and es > 3:
            pagmat += 0.03 * pat
        
        resultado = f"El estudiante con número de inscripción {ni}, nombre {nom}, debe pagar: ${pagmat:,.2f}"
        label_resultado.config(text=resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos en todos los campos.")

root = tk.Tk()
root.title("Cálculo de Pago de Matrícula")
root.geometry("500x400")

label_ni = tk.Label(root, text="Número de Inscripción:")
label_ni.pack(pady=5)
entry_ni = tk.Entry(root)
entry_ni.pack(pady=5)

label_nom = tk.Label(root, text="Nombre del Estudiante:")
label_nom.pack(pady=5)
entry_nom = tk.Entry(root)
entry_nom.pack(pady=5)

label_pat = tk.Label(root, text="Patrimonio:")
label_pat.pack(pady=5)
entry_pat = tk.Entry(root)
entry_pat.pack(pady=5)

label_es = tk.Label(root, text="Estrato:")
label_es.pack(pady=5)
entry_es = tk.Entry(root)
entry_es.pack(pady=5)

btn_calcular = tk.Button(root, text="Calcular Matrícula", command=calcular_matricula)
btn_calcular.pack(pady=10)

label_resultado = tk.Label(root, text="Resultado: ", font=("Arial", 12), wraplength=450, justify="left")
label_resultado.pack(pady=10)

root.mainloop()
