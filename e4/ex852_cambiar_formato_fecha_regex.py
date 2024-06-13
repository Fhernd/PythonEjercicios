# Ejercicio 852: Cambiar el formato de una fecha con una expresión regular (regex).

# Fuente: AAAA/MM/DD
# Destino: DD-MM-AAAA

import re

def cambiar_formato(fecha):
    patron = r'(\d{4})/(\d{2})/(\d{2})'

    return re.sub(patron, '\\3-\\2-\\1', fecha)


fecha_registro = '2003/03/13'

print('Fecha con el formato original:', fecha_registro)

fecha_nuevo_formato = cambiar_formato(fecha_registro)

print('Fecha con el formato modificado:', fecha_nuevo_formato)
