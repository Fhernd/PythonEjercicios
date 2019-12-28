# Ejercicio 366: Calcular el nivel de profundidad de un objeto diccionario.

# {'a': {'b': 1, 'c': {'d': {}}}}

def profundidad_diccionario(diccionario):
    if isinstance(diccionario, dict):
        return 1 + (max(map(profundidad_diccionario, diccionario.values())) if diccionario else 0)
    return 0


d = {'a': {'b': 1, 'c': {'d': {}}}}

resultado = profundidad_diccionario(d)

print(resultado)
