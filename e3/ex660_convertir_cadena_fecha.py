# Ejercicio 660: Crear una función para convertir una cadena de caracteres a un objeto fecha.

from datetime import datetime

def convertir_cadena_a_fecha(cadena):
    fecha = datetime.strptime(cadena, '%b %d %Y %I:%M:%S')

    return fecha

cadena_fecha = 'Feb 22 2020 10:05:17'
fecha = convertir_cadena_a_fecha(cadena_fecha)

print(type(fecha))
print(fecha)
