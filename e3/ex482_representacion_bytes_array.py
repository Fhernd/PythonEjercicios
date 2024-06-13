# Ejercicio 482: Obtener la representación en bytes de un objeto array con tobytes().

from array import array

arreglo_bytes = array('b', [80, 121, 116, 104, 111, 110])

cadena_bytes = arreglo_bytes.tobytes()

print(cadena_bytes)
