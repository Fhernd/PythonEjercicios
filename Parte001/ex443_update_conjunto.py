# Ejercicio 443: Agregar múltiples elementos a un objeto conjunto con el método update().

colores = set()

colores.add('Negro')
colores.add('Blanco')

print(len(colores))
print(colores)

print()

lista_colores = ['Rojo', 'Verde', 'Azul', 'Rojo', 'Verde']

colores.update(lista_colores)

print(len(colores))
print(colores)
