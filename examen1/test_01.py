"""
1. Usando los tipos de datos y sus conversiones realizar lo siguiente. (3 ptos)
Reglas:
- Pedir por consola nombre y edad de un usuario.
- Edad tiene que ser tipo entero, para esto apoyarse de la conversión de datos
- Identificar los tipos de datos ingresados y mostrarlos en pantalla.
- Pedir los nombres y edades para dos trabajadores y finalmente
agregarlos a una lista. Mostrar la suma de las edades de los
trabajadores localizándolos por la posición en la lista.
"""

nombre=input("Ingrese su nombre: ")
edad= int(input("Ingrese su edad: "))

print(f"\nSu nombre es {nombre} y su edad es {edad}")
print(f"el tipo de dato del nombre es {type(nombre)} y el tipo de edad es {type(edad)}")


print("\nPARTE 2\n")

print("Ingrese datos de trabajador 1 y 2\n")

nombre_t1 = input("Ingrese su nombre: ")
edad_t1 = int(input("Ingrese su edad: "))

print(f"\nBuenas {nombre_t1}, su edad es {edad_t1}")
print("\nIngrese los datos del segundo trabajador\n")

nombre_t2 = input("Ingrese su nombre: ")
edad_t2 = int(input("Ingrese su edad: "))

print(f"\nBuenas {nombre_t2}, su edad es {edad_t2}")

lista = []

lista.append(nombre_t1)
lista.append(edad_t1)
lista.append(nombre_t2)
lista.append(edad_t2)

suma = lista[1] + lista[3]

print(f"La suma es de las edades de los 2 trabajadores es: {suma}")
