# Ejercicio 962: Sumar los dígitos de varios números contenidos en una lista usando la función chain() de itertools.

from itertools import chain

numeros = [10, 13, 19]

# Suma dígitos: 1 + 4 + 10 = 15

suma_digitos = sum(int(v) for v in (chain(*[str(n) for n in numeros])))

print(suma_digitos) # 15
