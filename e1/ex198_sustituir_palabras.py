# Ejercicio 198: Alternar la posición de dos palabras específicas en una cadena de caracteres.

# Solución:

print('Escriba un texto que incluya las palabras `Python` y `C++`: ', end='')
palabras = input().split()

for i in range(len(palabras)):
    if 'C++' in palabras[i]:
        palabras[i] = 'Python'
    elif 'Python' in palabras[i]:
        palabras[i] = 'C++'

print(*palabras)
