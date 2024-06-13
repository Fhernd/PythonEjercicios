# Ejercicio 20: Emular el funcionamiento del producto de cadenas.

def producto_cadena(cadena, repeticion):
    """
    Emula el funcionamiento del producto (*) de cadenas.
    """
    resultado = ""

    for i in range(repeticion):
        resultado += cadena
    
    return resultado


print('Python' * 3)
print(producto_cadena('Python', 3))
