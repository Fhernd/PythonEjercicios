# Ejercicio 343: Agregar un nuevo elemento antes de cada elemento de una lista.

# ['Rojo', 'Verde', 'Azul'] => ['c', 'Rojo', 'c', 'Verde', 'c', 'Azul']

def agregar_elemento_lista(lista, caracter):
    return [valor for e in lista for valor in (caracter, e)]


colores = ['Rojo', 'Verde', 'Azul']

resultado = agregar_elemento_lista(colores, 'c')

print(colores)
print(resultado)
