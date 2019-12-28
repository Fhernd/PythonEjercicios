# Ejercicio 213: Crear una función para calcular longitud de una cadena de caracteres sin usar len.

# Solución:

def calcular_longitud_cadena(cadena):
    """
    Calcula la longitud de una cadena de caracteres.
    """
    contador = 0

    for c in cadena:
        contador += 1
    
    return contador


texto = '¡Python es tremendo!'

print(len(texto))

print(calcular_longitud_cadena(texto))
