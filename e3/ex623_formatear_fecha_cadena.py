# Ejercicio 623: Cambiar el formato de una fecha representada como una cadena de caracteres.

# 02/12/2019 -> 20191202

def cambiar_formato_fecha(fecha):
    partes_fecha = fecha.split('/')

    return '{}{}{}'.format(partes_fecha[2], partes_fecha[1], partes_fecha[0])

print(cambiar_formato_fecha('02/12/2019'))
print(cambiar_formato_fecha('14/02/2020'))
