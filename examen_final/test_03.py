import datetime


def medidor_tiempo(funcion):
    def wrapper(*args, **kwargs):
        inicio = datetime.datetime.now()
        resultado = funcion(*args, **kwargs)
        fin = datetime.datetime.now()
        tiempo_transcurrido = fin - inicio
        print(f"El tiempo de ejecución de"
              f" '{funcion.__name__}': {tiempo_transcurrido} segundos")
        return resultado
    return wrapper


@medidor_tiempo
def multiplicacion(*numeros):
    resultado = 1
    for num in numeros:
        resultado *= num
    return resultado


# EJEMPLOS
print(multiplicacion(36, 65, 987))
print(multiplicacion(0, 1, 54, 7))
print(multiplicacion(54, 3, 1, 321))
