# Ejercicio 300: Crear función para ordenar un grupo de tuplas a partir del último elemento.

def ordenar_lista_tuplas(tuplas):
    return sorted(tuplas, key=lambda t: t[-1])


listado = [(2, 7), (3, 11), (5, 2), (11, 9)]

resultado = ordenar_lista_tuplas(listado)

print(listado)
print(resultado)
