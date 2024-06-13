# Ejercicio 494: Crear el siguiente patrón usando un ciclo for anidado.

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

n = 5

for i in range(1, n + 1):
    for j in range(i):
        print('* ', end='')
    print()

for i in range(n - 1, 0, -1):
    for j in range(i):
        print('* ', end='')
    print()
