# Ejercicio 437: Remover las tuplas vacías desde una lista de tuplas.

tuplas = [(1, 2), (5,), (), (9, 8, 7), (1,), (), ()]

print(tuplas)
print(len(tuplas))

print()

tuplas = [t for t in tuplas if t]

print(tuplas)
print(len(tuplas))
