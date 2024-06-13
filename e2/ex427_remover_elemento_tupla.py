# Ejercicio 427: Crear una función para remover un elemento de un objeto tupla.

def remover_elemento(tupla, i):
    if 0 <= i < len(tupla):
        return tupla[0:i] + tupla[i+1:]

    raise ValueError('i está por fuera del rango.')


numeros = (2, 3, 5, 7)
indice = 1

resultado = remover_elemento(numeros, indice)

print(numeros)
print(resultado)
