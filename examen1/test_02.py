"""2.Usando el concepto y funciones de listas, realizar un programa con
las siguiente características (3 ptos):
Reglas:
- Crear una lista con 10 valores random o aleatorios (Pista: Usar el método
append y for)
- Llenar otra lista con sus cubos.
- Llenar una lista nueva con sus cuadrados.
- Mostrar de manera inversa la suma de ambas listas creadas."""
import random

lista = []
for _ in range(10):
    lista.append(random.randint(1, 100))

print(f"La lista con numeros aleatorios es {lista}")

lista_cubos = [num ** 3 for num in lista]

lista_cuadrao = [pow(num, 2) for num in lista]

print(f"La lista de los numeros al cubo es {lista_cubos}")
print(f"La lista de los numeros al cuadrado es {lista_cuadrao}")

lista_cubos.reverse()
lista_cuadrao.reverse()

print(f"La lista invertida de los numeros al cubo es {lista_cubos}")
print(f"La lista invertida  de los numeros al cuadrado es {lista_cuadrao}")

suma = sum(lista_cubos) + sum(lista_cuadrao)

print("La suma de ambas listas es: {}".format(suma))