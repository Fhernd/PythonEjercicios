# Ejercicio 489: Uso del método de instancia tostring() de la clase array.

from array import array

numeros = array('i', [2, 3, 5, 7])
cadena = numeros.tostring()
print(cadena)

print()

primos = array('i')
primos.fromstring(cadena)
print(primos)
