# Ejercicio 590: Convertir un arreglo de bytes a un objeto array con frombytes().

from array import array
from binascii import hexlify

primos = array('i', [2, 3, 5, 7, 11])
print(primos)

print()

arreglo_bytes = primos.tobytes()
print(hexlify(arreglo_bytes))

print()

primos_2 = array('i')
primos_2.frombytes(arreglo_bytes)
print(primos_2)
