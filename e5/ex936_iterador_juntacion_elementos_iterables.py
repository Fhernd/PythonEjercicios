# Ejercicio 936: Crear un iterador que junte elementos desde dos colecciones hasta donde sea posible.

# C1: ABCD
# C2: XY
# AX, BY, C*, D*

from itertools import zip_longest

resultado = list(zip_longest('ABCD', 'xy', fillvalue='*'))
print(resultado)

print()

resultado = list(zip_longest('xy', 'ABCD', fillvalue='*'))
print(resultado)

print()

resultado = list(zip_longest('xy', 'ABCD', ['M', 'N', 'O'], fillvalue='*'))
print(resultado)
