import random


def num_aleatorio():
    lista = [random.randint(1, 10) for i in range(10)]
    print("\n↓↓↓↓ Lista de números aleatorios ↓↓↓↓")
    print(lista)
    return lista


def no_repetidos(lista):
    lista_no_repetidos = list(set(lista))
    print("\n↓↓↓↓ Esta es la lista de los números no repetidos ↓↓↓↓")
    print(lista_no_repetidos)
    return lista_no_repetidos


def ordenar(lista):
    lista_ordenada_ascendente = sorted(lista)
    lista_ordenada_descendente = sorted(lista, reverse=True)
    print("\n↓↓↓↓ Lista ordenada de menor a mayor ↓↓↓↓")
    print(lista_ordenada_ascendente)
    print("\n↓↓↓↓ Lista ordenada de mayor a menor ↓↓↓↓")
    print(lista_ordenada_descendente)
    return lista_ordenada_ascendente, lista_ordenada_descendente


def mayor_num(lista):
    num_pares = [num for num in lista if num % 2 == 0]
    if num_pares:
        maximo_par = max(num_pares)
        print("\n↓↓↓↓ El mayor número par de la lista es ↓↓↓↓")
        print(maximo_par)
        return maximo_par
    else:
        print("\nNo hay números pares en la lista")
        return None
