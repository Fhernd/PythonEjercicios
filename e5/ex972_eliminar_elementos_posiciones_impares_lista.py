# Ejercicio 972: Eliminar los valores que se hallen en las posiciones impares de una lista.

letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(letras)

print()

letras = [letras[i] for i in range(len(letras)) if i % 2 == 0]
print(letras) # ['A', 'C', 'E', 'G', 'I']
