# Ejercicio 768: Usar el módulo random para generar 10000 lanzamientos de una moneda.

import random

resultados = {'sello': 0, 'cara': 0}

lados = list(resultados.keys())

for _ in range(10000):
    resultados[random.choice(lados)] += 1

print('Sellos:', resultados['sello'])
print('Caras:', resultados['cara'])
