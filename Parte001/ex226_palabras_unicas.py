# Ejercicio 226: Obtener las palabras únicas de un listado de palabras definido por el usuario.

entrada = input('Digite un grupo de palabras separadas por coma: ')

palabras = entrada.split(',')

print(palabras)

palabras_unicas = list(set(palabras))

print(palabras_unicas)
