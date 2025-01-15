import tkinter as tk
from tkinter import messagebox
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio**2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def dibujar(self, canvas):
        canvas.create_oval(150 - self.radio, 150 - self.radio, 
                           150 + self.radio, 150 + self.radio, outline="black", width=2)


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

    def dibujar(self, canvas):
        canvas.create_rectangle(150 - self.base / 2, 150 - self.altura / 2, 
                                150 + self.base / 2, 150 + self.altura / 2, outline="black", width=2)


class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado**2

    def calcular_perimetro(self):
        return 4 * self.lado

    def dibujar(self, canvas):
        canvas.create_rectangle(150 - self.lado / 2, 150 - self.lado / 2, 
                                150 + self.lado / 2, 150 + self.lado / 2, outline="black", width=2)


class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_perimetro(self):
        return self.base + self.altura + self.calcular_hipotenusa()

    def calcular_hipotenusa(self):
        return math.sqrt(self.base**2 + self.altura**2)

    def determinar_tipo_triangulo(self):
        hipotenusa = self.calcular_hipotenusa()
        if self.base == self.altura == hipotenusa:
            return "Equilátero"
        elif self.base != self.altura != hipotenusa and self.base != hipotenusa:
            return "Escaleno"
        else:
            return "Isósceles"

    def dibujar(self, canvas):
        canvas.create_polygon(150, 150, 150 + self.base, 150, 150, 150 - self.altura, outline="black", width=2, fill="gray")


def calcular_figura():
    figura = figura_var.get()

    try:
        if figura == 'Círculo':
            radio = float(entry_parametro.get())
            circulo = Circulo(radio)
            area = circulo.calcular_area()
            perimetro = circulo.calcular_perimetro()
            resultado = f"Área: {area:.2f}\nPerímetro: {perimetro:.2f}"

            ventana_figura = tk.Toplevel(ventana)
            ventana_figura.title("Dibujar Círculo")
            canvas_figura = tk.Canvas(ventana_figura, width=400, height=400, bg="white")
            canvas_figura.pack()
            circulo.dibujar(canvas_figura)

        elif figura == 'Rectángulo':
            base = float(entry_parametro1.get())
            altura = float(entry_parametro2.get())
            rectangulo = Rectangulo(base, altura)
            area = rectangulo.calcular_area()
            perimetro = rectangulo.calcular_perimetro()
            resultado = f"Área: {area:.2f}\nPerímetro: {perimetro:.2f}"

            ventana_figura = tk.Toplevel(ventana)
            ventana_figura.title("Dibujar Rectángulo")
            canvas_figura = tk.Canvas(ventana_figura, width=400, height=400, bg="white")
            canvas_figura.pack()
            rectangulo.dibujar(canvas_figura)

        elif figura == 'Cuadrado':
            lado = float(entry_parametro.get())
            cuadrado = Cuadrado(lado)
            area = cuadrado.calcular_area()
            perimetro = cuadrado.calcular_perimetro()
            resultado = f"Área: {area:.2f}\nPerímetro: {perimetro:.2f}"

            ventana_figura = tk.Toplevel(ventana)
            ventana_figura.title("Dibujar Cuadrado")
            canvas_figura = tk.Canvas(ventana_figura, width=400, height=400, bg="white")
            canvas_figura.pack()
            cuadrado.dibujar(canvas_figura)

        elif figura == 'Triángulo Rectángulo':
            base = float(entry_parametro1.get())
            altura = float(entry_parametro2.get())
            triangulo = TrianguloRectangulo(base, altura)
            area = triangulo.calcular_area()
            perimetro = triangulo.calcular_perimetro()
            tipo = triangulo.determinar_tipo_triangulo()
            resultado = f"Área: {area:.2f}\nPerímetro: {perimetro:.2f}\nTipo: {tipo}"

            ventana_figura = tk.Toplevel(ventana)
            ventana_figura.title("Dibujar Triángulo Rectángulo")
            canvas_figura = tk.Canvas(ventana_figura, width=400, height=400, bg="white")
            canvas_figura.pack()
            triangulo.dibujar(canvas_figura)

        else:
            messagebox.showerror("Error", "Selecciona una figura válida")
            return

        messagebox.showinfo("Resultados", resultado)

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")


ventana = tk.Tk()
ventana.title("Calculadora y Dibujador de Figuras Geométricas")

figura_var = tk.StringVar()

etiqueta_figura = tk.Label(ventana, text="Selecciona la figura")
etiqueta_figura.grid(row=0, column=0, pady=10)

opciones_figura = ['Círculo', 'Rectángulo', 'Cuadrado', 'Triángulo Rectángulo']
menu_figura = tk.OptionMenu(ventana, figura_var, *opciones_figura)
menu_figura.grid(row=0, column=1, pady=10)

etiqueta_parametros = tk.Label(ventana, text="Ingresa los parámetros de la figura")
etiqueta_parametros.grid(row=1, column=0, columnspan=2, pady=10)

entry_parametro1 = None
entry_parametro2 = None
entry_parametro = None

def actualizar_parametros(*args):
    global entry_parametro1, entry_parametro2, entry_parametro
    for widget in frame_parametros.winfo_children():
        widget.destroy()

    figura = figura_var.get()

    if figura == 'Círculo':
        etiqueta_radio = tk.Label(frame_parametros, text="Radio:")
        etiqueta_radio.grid(row=0, column=0)
        entry_parametro = tk.Entry(frame_parametros)
        entry_parametro.grid(row=0, column=1)

    elif figura == 'Rectángulo':
        etiqueta_base = tk.Label(frame_parametros, text="Base:")
        etiqueta_base.grid(row=0, column=0)
        entry_parametro1 = tk.Entry(frame_parametros)
        entry_parametro1.grid(row=0, column=1)

        etiqueta_altura = tk.Label(frame_parametros, text="Altura:")
        etiqueta_altura.grid(row=1, column=0)
        entry_parametro2 = tk.Entry(frame_parametros)
        entry_parametro2.grid(row=1, column=1)

    elif figura == 'Cuadrado':
        etiqueta_lado = tk.Label(frame_parametros, text="Lado:")
        etiqueta_lado.grid(row=0, column=0)
        entry_parametro = tk.Entry(frame_parametros)
        entry_parametro.grid(row=0, column=1)

    elif figura == 'Triángulo Rectángulo':
        etiqueta_base = tk.Label(frame_parametros, text="Base:")
        etiqueta_base.grid(row=0, column=0)
        entry_parametro1 = tk.Entry(frame_parametros)
        entry_parametro1.grid(row=0, column=1)

        etiqueta_altura = tk.Label(frame_parametros, text="Altura:")
        etiqueta_altura.grid(row=1, column=0)
        entry_parametro2 = tk.Entry(frame_parametros)
        entry_parametro2.grid(row=1, column=1)

frame_parametros = tk.Frame(ventana)
frame_parametros.grid(row=2, column=0, columnspan=2, pady=10)

figura_var.trace("w", actualizar_parametros)

boton_calcular = tk.Button(ventana, text="Calcular y Dibujar", command=calcular_figura)
boton_calcular.grid(row=3, column=0, columnspan=2, pady=10)

ventana.mainloop()
