# Ejercicio 470: Encontrar el nombre de lenguaje de programación más común con Counter.

from collections import Counter

lenguajes = ['Python', 'C', 'C', 'PHP', 'Python', 'Java', 'Python', 'C++', 'JavaScript', 'Python', 'Perl', 'Java']

contador = Counter(lenguajes)

print(contador)

print(contador.most_common(1)[0][0])
