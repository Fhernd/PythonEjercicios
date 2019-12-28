# Ejercicio 345: Convertir una lista en una lista de diccionarios.

nombres_colores = ['Blanco', 'Negro', 'Rojo', 'Verde', 'Azul']
codigos_colores = ['#FFFFFF', '#000000', '#FF0000', '#00FF00', '#0000FF']

colores = [{'nombre': n, 'codigo': c} for n, c in zip(nombres_colores, codigos_colores)]

print(colores)
