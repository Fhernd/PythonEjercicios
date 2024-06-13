# Ejercicio 270: Poner en mayúscula el primer y último carácter de cada palabra en una frase.

# 'python es genial' => 'PythoN ES GeniaL'

def mayusculas_primer_ultimo_caracter(frase):
    resultado = ''

    for p in frase.split():
        resultado += p[0].upper() + p[1:-1] + p[-1].upper() + ' '

    return resultado


texto = 'python es genial'
print(texto)
print(mayusculas_primer_ultimo_caracter(texto))
