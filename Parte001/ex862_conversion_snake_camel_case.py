# Ejercicio 862: Convertir el nombre de una variable de modo snake case a camel case.

# Snake case: nombre_variable
# Camel case: NombreVariable

def conversion_case(nombre_variable):
    return ''.join(p.capitalize() for p in nombre_variable.split('_'))

print(conversion_case('nombre_variable'))
print(conversion_case('edad_persona'))
