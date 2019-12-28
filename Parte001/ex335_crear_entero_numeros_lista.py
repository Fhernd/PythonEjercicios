# Ejercicio 335: Crear un número entero único a partir de la unión de un listado de números.

# [1, 2, 3, 4, 5] => 12345

def union_listado_enteros(numeros):
    concatenacion = ''.join(map(str, numeros))

    return int(concatenacion)


numeros = [1, 2, 3, 4, 5]
resultado = union_listado_enteros(numeros)
print(numeros)
print(resultado)
