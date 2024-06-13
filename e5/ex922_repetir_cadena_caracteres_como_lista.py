# Ejercicio 922: Repetir n veces una cadena de caracteres como una lista de caracteres con la función tee().

from itertools import tee

lenguaje = 'Python'
print(lenguaje)

print()

resultado = tee(lenguaje, 5)

for r in resultado:
    print(list(r))
