import math

class Tarea_1:
    """
    TAREA 1
    Curso: Programación Orientada a Objetos
    Grupo: 3
    Semestre: 2024-2
    Profesor: Walter Hugo Arboleda Mazo
    """
    def ejercicioR4(self):
        edad_juan = float(input("ingrese la edad de juan: "))
        edad_alberto = (2 / 3) * edad_juan
        edad_ana = (4 / 3) * edad_juan
        edad_madre = edad_juan + edad_alberto + edad_ana
        print("Juan tiene {:.2f} años".format(edad_juan),
            "\nAlberto tiene {:.2f} años".format(edad_alberto),
            "\nAna tiene {:.2f} años".format(edad_ana),
            "\nla madre tiene {:.2f} años".format(edad_madre))
    
    def ejercicioR5(self):
        suma = 0
        equis = 20
        suma = suma + equis
        ye = 40
        equis = equis + ye ** 2
        suma = suma + equis / ye
        print("el valor de la suma es ", suma)

    def ejercicioP12(self):
        sal_bruto = 45 * 5000
        retencion = 0.125 * sal_bruto
        sal_neto = sal_bruto - retencion
        print("salario bruto: $ {:.2f}".format(sal_bruto),
              "\ncantidad de retencion: $ {:.2f}".format(retencion),
              "\nsalario neto: $ {:.2f}".format(sal_neto))
        
    def ejercicioP14(self):
        numero = float(input("numero: "))
        cuadrado = numero ** 2
        cubo = numero ** 3
        print("cuadrado: {:.2f}\ncubo: {:.2f}".format(cuadrado, cubo))

    def ejercicioP17(self):
        radio = float(input("radio: "))
        circun = 2 * math.pi * radio
        area = math.pi * radio ** 2
        print("circunferencia: {:.2f}\narea: {:.2f}".format(circun, area))

    def menu(self):
        opciones = [
            (self.ejercicioR4, "ejercicio resuelto 4\t"),
            (self.ejercicioR5, "ejercicio resuelto 5"),
            (self.ejercicioP12, "ejercicio propuesto 12"),
            (self.ejercicioP14, "ejercicio propuesto 14"),
            (self.ejercicioP17, "ejercicio propuesto 17")
        ]
        
        while True:
            mensaje = "\nseleccione el ejercicio que desea ejecutar:\n"
            for i, (_, descripcion) in enumerate(opciones, start=1):
                if i % 2:
                    mensaje += f"\n{i}. {descripcion}"
                else:
                    mensaje += f"\t{i}. {descripcion}"
            mensaje += "\t6. salir"
            print(mensaje+"\n")

            opcion = input("selección: ")

            if opcion.isdigit() and int(opcion) in range(1, len(opciones) + 1):
                print("\n" + opciones[int(opcion) - 1][1] + "\n")
                opciones[int(opcion) - 1][0]()
            elif opcion.isdigit() and int(opcion) == 6:
                break
            else:
                print("\nintentalo nuevamente...")


if __name__ == "__main__":
    actividades = Tarea_1()
    actividades.menu()
