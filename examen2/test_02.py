"""
2. Usando el concepto de herencia y encapsulación (para saldo) para crear el siguiente programa (3 ptos):
Reglas:
- Agregar un atributo saldo a la clase persona (ejercicio anterior).
- Crear un método transferencia y mostrar saldo (mostrará el saldo actual que tiene la persona) para la clase mencionada
- El método transferencia hace que la Persona que llame al método pueda transferir la cantidad monto al objeto Persona2 por consiguiente deberá ir actualizando también el saldo o monto
    que tiene la otra persona en su cuenta cada vez que use el método transferencia
- Comprobar si no se tiene dinero suficiente no se ejecuta la acción e imprimir “Saldo insuficiente”. Comprobar instanciado la clase por lo menos realizando una transferencia y con dos personas.
"""

"""EJERCICIO 1"""

import datetime
class Persona:
    def __init__(self):
        self.nombre = ""
        self.edad = None
        self.saldo = 1000
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





"""EJERCICIO 2 """

class PersonaTransferencia(Persona):

    def __init__(self):
        super().__init__()
        self.__saldo = 1000
    def transferencia(self, destinatario, monto):
        if self.__saldo >= monto:
            self.__saldo -= monto
            destinatario.__saldo += monto
            print(f"Transferencia de {monto} soles a {destinatario.nombre} realizada.")
        else:
            print("Saldo insuficiente.")

    def mostrar_saldo(self):
        print(f"El saldo de {self.nombre} es: {self.__saldo} soles.")


perso1 = PersonaTransferencia()
perso1.nombre_edad()
perso1.cumpleanos()
perso1.mostrar_fecha_hora_registro()


perso2 = PersonaTransferencia()
perso2.nombre_edad()
perso2.cumpleanos()
perso1.mostrar_fecha_hora_registro()

perso1.__saldo = 1000  # Modificación directa del saldo (simula una entrada incorrecta)
perso1.mostrar_saldo()
perso1.transferencia(perso2, 500)  # Intento de transferencia
perso1.mostrar_saldo()
perso2.mostrar_saldo()
