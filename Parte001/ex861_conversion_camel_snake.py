# Ejercicio 861: Convertir el nombre de una variable de modo camel case a snake case.

# Camel case: NombreVariable
# Snake case: nombre_variable

import re

def conversion_case(nombre_variable):
    conversion = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', nombre_variable)

    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', conversion).lower()


print(conversion_case('NombreVariable'))
