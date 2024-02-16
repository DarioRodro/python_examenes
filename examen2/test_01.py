"""
1. Escriba un programa donde tendrá los siguientes requisitos (4 ptos):
Reglas:
- Crear una clase llamada Persona donde sus atributos deben ser nombre, edad, saldo y de nacionalidad peruana (use el manejo de errores para el tipo de dato) y un método para solicitar su nombre y edad.
- Tendrá un método cumpleaños donde cada vez que invoque aumentará en un año la edad de la persona.
- Crear la instancia de la clase Persona y usar su método cumpleaños para incrementar su edad (mínimo instanciar la clase 2 veces, mostrar por pantalla dicha edad actualizada).
- Crear una función que retorne solamente la fecha, hora y minuto que se ha registrado esta persona (Mostrar por pantalla este valor)

"""
import datetime
class Persona:
    def __init__(self):
        self.nombre = ""
        self.edad = None
        self.saldo = 0
        self.nacionalidad = "peruana"

    def nombre_edad(self):
        self.nombre = input("Ingrese su nombre: ")
        while True:
            edad = int(input("Ingrese su edad: "))
            try:
                self.edad = int(edad)
                if edad <= 0:
                    raise ValueError("La edad debe ser mayor a 0")
                break
            except ValueError:
                print("Error: La edad debe ser un número natural o entero positivo")

    def cumpleanos(self):
        if self.edad is not None:
            self.edad += 1
            print(f"Ahora {self.nombre} tiene {self.edad} de edad")


    def mostrar_fecha_hora_registro(self):
        print("Fecha y hora de registro:", self.obtener_fecha_hora_actual())


    def obtener_fecha_hora_actual(self):
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")

perso1 = Persona()
perso1.nombre_edad()
perso1.cumpleanos()
perso1.mostrar_fecha_hora_registro()

perso2 = Persona()
perso2.nombre_edad()
perso2.cumpleanos()
perso2.mostrar_fecha_hora_registro()








