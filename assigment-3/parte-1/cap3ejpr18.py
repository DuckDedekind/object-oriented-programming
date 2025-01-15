import tkinter as tk
from tkinter import messagebox

class EmpleadoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cálculo de Salarios de Empleado")

        tk.Label(root, text="Código del empleado:").grid(row=0, column=0, sticky="w")
        self.codigo_entry = tk.Entry(root)
        self.codigo_entry.grid(row=0, column=1)

        tk.Label(root, text="Nombres:").grid(row=1, column=0, sticky="w")
        self.nombres_entry = tk.Entry(root)
        self.nombres_entry.grid(row=1, column=1)

        tk.Label(root, text="Horas trabajadas al mes:").grid(row=2, column=0, sticky="w")
        self.horas_entry = tk.Entry(root)
        self.horas_entry.grid(row=2, column=1)

        tk.Label(root, text="Valor por hora:").grid(row=3, column=0, sticky="w")
        self.valor_hora_entry = tk.Entry(root)
        self.valor_hora_entry.grid(row=3, column=1)

        tk.Label(root, text="Porcentaje de retención (%):").grid(row=4, column=0, sticky="w")
        self.retencion_entry = tk.Entry(root)
        self.retencion_entry.grid(row=4, column=1)

        self.calcular_button = tk.Button(root, text="Calcular", command=self.calcular_salarios)
        self.calcular_button.grid(row=5, column=0, columnspan=2)

    def calcular_salarios(self):
        try:
            codigo = self.codigo_entry.get()
            nombres = self.nombres_entry.get()
            horas_trabajadas = int(self.horas_entry.get())
            valor_hora = float(self.valor_hora_entry.get())
            retencion = float(self.retencion_entry.get()) / 100

            if not codigo or not nombres:
                raise ValueError("Debe ingresar el código y los nombres del empleado.")
            if horas_trabajadas <= 0 or valor_hora <= 0 or retencion < 0:
                raise ValueError("Los valores numéricos deben ser positivos.")

            salario_bruto = horas_trabajadas * valor_hora
            salario_neto = salario_bruto * (1 - retencion)

            resultado = (
                f"Código: {codigo}\n"
                f"Nombres: {nombres}\n"
                f"Salario Bruto: ${salario_bruto:.2f}\n"
                f"Salario Neto: ${salario_neto:.2f}"
            )
            messagebox.showinfo("Resultados", resultado)

        except ValueError as e:
            messagebox.showerror("Error", f"Entrada inválida: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmpleadoApp(root)
    root.mainloop()
