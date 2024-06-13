# Ejercicio 256: Pasar a mínusculas los primeros n caracteres.

def poner_minusculas(cadena, n):
    return cadena[:n].lower() + cadena[n:]


texto = 'PYTHON ES GÉNIAL'

print(poner_minusculas(texto, 6))
