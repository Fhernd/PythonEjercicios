# Ejercicio 567: Crear una función lambda para determinar si una cadena es un número.

es_numero = lambda n: n.replace('.', '', 1).isdigit()

print(es_numero('123.456'))
print(es_numero('123.456a'))
print(es_numero('-123.456'))
print(es_numero('123'))
