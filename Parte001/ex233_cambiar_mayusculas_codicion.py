# Ejercicio 233: Cambiar a mayúsculas un texto si hay al menos dos caracteres en mayúscula.

# Descripción: Cambiar a mayúsculas un texto si hay al menos dos caracteres en mayúscula en los primeros cuatro caracteres.

# Análisis:

# Python
# PYthon => PYTHON

def cambiar_mayusculas(cadena):
    if len(cadena) > 4:

        contador = 0

        for i in range(4):
            if cadena[i] == cadena[i].upper():
                contador += 1
        
        if contador >= 2:
            return cadena.upper()
        else:
            return cadena
    else:
        return cadena


texto = 'Python'
print(cambiar_mayusculas(texto))

texto = 'PyThon'
print(cambiar_mayusculas(texto))
