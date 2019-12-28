# Ejercicio 267: Remover todo el espacio de una cadena de caracteres.

def remover_espacio(cadena):
    return cadena.replace(' ', '')


url = '  https :// www.python. org'

print(url)
print(remover_espacio(url))
