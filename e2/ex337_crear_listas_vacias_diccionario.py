# Ejercicio 337: Crear un diccionario de n listas vacías.

def crear_diccionario_listas(n):
    diccionario = {}

    for i in range(1, n + 1):
        diccionario[i] = []
    
    return diccionario


resultado = crear_diccionario_listas(10)

print(resultado)
