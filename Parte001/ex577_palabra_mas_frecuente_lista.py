# Ejercicio 577: Encontrar la palabra más frecuente en una lista de cadenas de caracteres.

from collections import Counter

colores = [
   'Rojo', 'Verde', 'Negro', 'Rosado', 'Negro', 'Blanco', 'Negro', 'eyes',
   'Blanco', 'Negro', 'Naranja', 'Rosado', 'Rosado', 'Rojo', 'Rojo', 'Blanco', 'Naranja',
   'Blanco', "Negro", 'Rosado', 'Verde', 'Verde', 'Rosado', 'Verde', 'Rosado',
   'Blanco', 'Naranja', "Naranja", 'Rojo'
]

contador = Counter(colores)
color_mas_repetido = contador.most_common(1)
print(color_mas_repetido)
