# Ejercicio 579: Contar el número de ocurrencias de nombres de lenguajes de programación.

from collections import Counter

lenguajes = (('Python', '2'), ('Python', '3'), ('Java', '6'), ('Java', '7'), ('Java', '8'), ('C#', '5'), ('C#', '6'), ('C#', '7'), ('Java', '12'))

ocurrencias = Counter(l for l, v in lenguajes)

print(ocurrencias)
