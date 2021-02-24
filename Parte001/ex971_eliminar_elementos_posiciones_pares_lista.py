# Ejercicio 971: Eliminar los valores que se hallen las posiciones pares de una lista.

letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(letras)

# [B, D, F, H, J]

print()

letras = [letras[i] for i in range(len(letras)) if i % 2 == 1]
print(letras)
