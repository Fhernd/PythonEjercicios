# Ejercicio 550: Crear una función para crear una frase ordenada separada por guiones.

def separar_frase_guiones(frase):
    frase = frase.split()
    frase.sort()
    return '-'.join(frase)


cadena = 'python java c++ php c javascript'
print(cadena)
resultado = separar_frase_guiones(cadena)
print(resultado)
