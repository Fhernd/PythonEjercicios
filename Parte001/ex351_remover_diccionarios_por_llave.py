# Ejercicio 351: Remover diccionarios de una lista cuya llave sea igual a un valor dado.

productos = [{'nombre': 'Teclado', 'categoria': 'Periférico'}, {'nombre': 'Mouse', 'marca': 'Logitech'}, {'nombre': 'Parlantes', 'categoria': 'Periférico'}]

print(productos)

llave = 'categoria'

resultado = [p for p in productos if llave not in p.keys()]

print()

print(resultado)
