"""
3. Escribir un programa para gestionar los errores en Python (3 ptos):
Reglas:
- El programa deberá tener una función para ingresar dos datospor consola.
- Deberá tener una función en el caso haya una división entre cero mencionar el error.
- Deberá tener una función la cuál evaluará la suma de datos incorrectos, mencionar el error
- Deberá tener una función donde se ingresarán N datos a una lista y al momento de pedir un índice incorrecto para mostrarlo en consola y no exista respectivamente ese
    índice, aplicar try, except respectivamente.
- Todas las funciones creadas tendrán la facultad de volver a pedir el número hasta que se ingresen correctamente.
"""

def datos():
    while True:
        try:
            dt1 = int(input("Introduce el primer dato: "))
            dt2 = int(input("Introduce el segundo dato: "))
            return dt1, dt2
        except ValueError:
            print("ERROR!!!: Por favor ingrese números enteros ")
def division(dt1, dt2):
    try:
        resultado= dt1 /dt2
        print(f"La división de estos datos es: {resultado}")
    except ZeroDivisionError:
        print("ERROR!!!: No se puede dividir entre 0")

def suma(dt1, dt2):
    try:
        resultado= dt1 + dt2
        print(f"La suma de los datos es: {resultado}")
    except TypeError:
        print("ERROR!!!: Estos datos no se pueden sumar ya que son diferentes tipos de datos")

def lista():
    lista = []
    while True:
            dato = input("Introduce un dato a la lista. Si desea terminar de ingresar datos, escriba 'sanma': ")
            if dato == "sanma":
                break
            lista.append(dato)
            print(f"Su listae es: {lista}")

    while True:
        try:
            indice = int(input("\nIngrese un índice para obtener el dato correspondiente: "))
            print("El dato en el índice", indice, "es:", lista[indice])
            break
        except IndexError:
            print("ERROR!!: No existe un dato dentro de ese índice")

print(">>>>>INGRESAR DATOS<<<<<")
dt1, dt2 = datos()

print("\n>>>>>DIVISIÓN DE DATOS<<<<<")
division(dt1, dt2)

print("\n>>>>>EVALUACIÓN DE SUMA<<<<<")
suma(dt1, dt2)

print("\n>>>>>INGRESAR DATOS A LA LISTA<<<<<")
lista()

