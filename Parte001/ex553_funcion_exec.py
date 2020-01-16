# Ejercicio 553: Crear función para ejecutar código como cadena de caracteres.

def ejecutar_codigo(cadena):
    exec(cadena)


codigo = 'print("Python")'
ejecutar_codigo(codigo)

print()

codigo = """
def sumar(a, b):
    return a + b

print(sumar(2, 3))
"""

ejecutar_codigo(codigo)
