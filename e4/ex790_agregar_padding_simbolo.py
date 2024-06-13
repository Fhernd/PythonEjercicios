# Ejercicio 790: Agregar padding al signo de un valor numérico en una cadena de formato.

# -13.19
# -    13.19
# 13.19
# +    13.19

numero = -13.19

print(numero)
print('{:=10.2f}'.format(numero))

print()

numero = 13.19
print(numero)
print('{:=+10.2f}'.format(numero))
