# Ejercicio 1025: Usar la función join() para unir una lista de palabras usando un separador específico.

def unir_palabras(palabras, separador=' '):
    resultado = separador.join(palabras)

    return resultado


lenguajes = ['Python', 'JavaScript', 'Go', 'PHP', 'C++', 'Java']
print(unir_palabras(lenguajes))
print(unir_palabras(lenguajes, ','))
print(unir_palabras(lenguajes, ', '))
print(unir_palabras(lenguajes, ':'))
