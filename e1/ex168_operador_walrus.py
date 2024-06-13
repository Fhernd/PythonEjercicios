# Ejercicio 168: Uso básico del operador walrus de Python 3.8.0.

# :=

cadena = 'Python'

if (l := len(cadena)) > 5:
    print(f'La cadena de caracteres {cadena} tiene más de 5 caracteres; exactamente {l}')
