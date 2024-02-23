import random
import math


def lista(tamano):
    lista = [random.randint(1, 100) for i in range(tamano)]
    with open("notas.txt", "a") as file:
        file.write("Lista con números aleatorios:\n")
        file.write(", ".join(map(str, lista)) + "\n")


# Con with, los ficheros se cierran una vez que termina ese bloque


def raices():
    with open("notas.txt", "a") as file:
        file.write("Raíces cuadradas:\n")
        with open("notas.txt", "r") as read_file:
            for line in read_file:
                numeros = line.strip().split(", ")
                for numero in numeros:
                    try:
                        raiz = math.sqrt(float(numero))
                        file.write(str(raiz) + "\n")
                    except ValueError:
                        pass
