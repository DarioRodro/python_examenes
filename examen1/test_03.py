"""3. Teniendo presente el uso y concepto de diccionarios en Python, realizar un
programa con los siguientes requerimientos (4 ptos)
Reglas:
- Crear un diccionario con los keys de nombre, apellidos, edad y dni.
- Pedir por consola los valores para estos keys.
- Mostrar en pantalla sólo los values del diccionario
- Agregar un key adicional con el nombre de “profesion” y un valor para este key
nuevo.
- Eliminar el key dni y mostrar el nuevo diccionario."""

diccionario = {}

diccionario['nombre'] = input('Ingrese su nombre: ')
diccionario['apellidos'] = input('Ingrese su apellido: ')
diccionario['edad'] = int(input('Ingrese su edad: '))
diccionario['dni'] = int(input('Ingrese su dni: '))

print("Los valores introduccidos al diccionario son: ")
for value in diccionario.values():
    print(value)

diccionario['profesion'] = input('Ingrese su profesion: ')

del diccionario['dni']

print(f"Al eliminar el key de dni, el nuevo diciconario es el siguiente : {diccionario}")