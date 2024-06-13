# Ejercicio 772: Obtener el listado de variables creadas en un script.

def mostrar_listado_variables(variables):
    for v in variables:
        if not v.startswith('__'):
            print(v)

mostrar_listado_variables(dir())

print()

a = 2
b = 3

mostrar_listado_variables(dir())
