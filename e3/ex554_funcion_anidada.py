# Ejercicio 554: Crear una función para invocar una función anidada.

def funcion_externa(a):
    def funcion_anidada(b):
        nonlocal a
        a += 1
        return a + b
    
    return funcion_anidada


resultado = funcion_externa(2)
print(resultado)
print(resultado(3))
