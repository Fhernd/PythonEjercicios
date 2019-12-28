# Ejercicio 306: Remover elementos de una lista que se hallen en índices específicos.

lenguajes = ['Python', 'JavaScript', 'C', 'Java', 'C++', 'PHP', 'C#']

print(lenguajes)

indices = (2, 4, 6)

resultado = [lenguajes[i] for i in range(len(lenguajes)) if i not in indices]

print(resultado)
