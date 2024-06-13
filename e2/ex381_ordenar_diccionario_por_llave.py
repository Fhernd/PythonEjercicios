# Ejercicio 381: Ordenar un objeto diccionario a partir de su llave con la función sorted().

from operator import itemgetter

colores = {'Negro': '#000000', 'Blanco': '#FFFFFF', 'Rojo': '#FF0000', 'Verde': '#00FF00', 'Azul': '#0000FF'}

print(colores)

colores = dict(sorted(colores.items(), key=itemgetter(0)))

print(colores)
