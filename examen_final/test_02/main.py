import funciones
import os


def crear_fichero():
    if not os.path.exists('notas.txt'):
        with open('notas.txt', 'w') as file:
            file.write('Archivo de notas creado.\n')


def main():
    crear_fichero()
    tamano_lista = int(input('Ingrese el tamaño de la lista: '))
    funciones.lista(tamano_lista)
    funciones.raices()
    print("Operaciones completadas. Verificar el archivo de notas.")


if __name__ == '__main__':
    main()
