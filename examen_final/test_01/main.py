import operaciones


numeros_aleatorios = operaciones.num_aleatorio()

numeros_no_repetidos = operaciones.no_repetidos(numeros_aleatorios)

lista_ascendente, lista_descendente = operaciones.ordenar(numeros_no_repetidos)

operaciones.mayor_num(numeros_no_repetidos)
