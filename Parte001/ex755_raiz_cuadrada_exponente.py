# Ejercicio 755: Calcular la raíz cuadrada y el exponente de un objeto Decimal.

from decimal import Decimal

numero = Decimal(1.79)

raiz = numero.sqrt()
exp = numero.exp()

print(raiz)
print(exp)
