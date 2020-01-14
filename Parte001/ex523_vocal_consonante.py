# Ejercicio 523: Identificar si una letra ingresa por el usuario es una vocal o consonante.

def vocal_o_consonante(letra):
    if letra in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        return 'Vocal'
    elif letra in ('y', 'Y'):
        return 'Vocal/Consonante'
    else:
        return 'Consonante'


l = input('Escriba una letra cualquiera: ')

print(vocal_o_consonante(l))
