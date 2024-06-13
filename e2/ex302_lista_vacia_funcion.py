# Ejercicio 302: Crear una función personalizada para comprobar si una lista está vacía.

def lista_vacia(lista):
    return not lista


numeros = [2, 3, 5]
print(lista_vacia(numeros))

numeros.pop()
print(lista_vacia(numeros))

numeros.pop()
print(lista_vacia(numeros))

numeros.pop()
print(lista_vacia(numeros))

print()

print(lista_vacia([]))
