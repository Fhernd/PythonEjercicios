# Ejercicio 589: Convertir un objeto array a su representación máquina en bytes.

from array import array
from binascii import hexlify

primos = array('i', [2, 3, 5, 7, 11, 13])
print(primos)

print()

arreglo_bytes = primos.tobytes()
print(hexlify(arreglo_bytes))
