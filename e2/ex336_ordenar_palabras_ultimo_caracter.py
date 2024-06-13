# Ejercicio 336: Ordenar un grupo de palabras de forma ascendente por el último carácter.

def ordenar_palabras(palabras):
    return sorted(palabras, key=lambda p: p[-1])


lenguajes = ['Python', 'PHP', 'Java', 'JavaScript', 'C#', 'C++']
resultado = ordenar_palabras(lenguajes)

print(lenguajes)
print(resultado)
