# Ejercicio 272: Sumar los dígitos que aparezcan en una cadena de caracteres.

# Solución:

# 'Python v. 3.8.0' => 11

def sumar_digitos_cadena(frase):
    suma = 0

    for c in frase:
        if c.isdigit():
            suma += int(c)
    
    return suma


frase = 'Python v. 3.8.0'

print(frase)
print(sumar_digitos_cadena(frase))

frase = 'PHP v. 7.1.2'
print(frase)
print(sumar_digitos_cadena(frase))
