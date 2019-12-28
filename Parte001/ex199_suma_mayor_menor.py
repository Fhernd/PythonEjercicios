# Ejercicio 199: Computar la diferencia entre el valor menor y mayor de un número de 9 dígitos.

# Solución:

# 678961123
# Mayor -> 987663211
# Menor -> 112366789

# Diferencia = Abs(Mayor - Menor)

numero = ''

while len(numero) != 9:
    numero = input('Digite un número de 9 dígitos: ')

    try:
        int(numero)
    except ValueError as e:
        print('MENSAJE: Debe digitar un número.')
        numero = ''


digitos = list(numero)

menor = sorted([int(n) for n in digitos])
mayor = sorted([int(n) for n in digitos], reverse=True)

menor = int(''.join([str(d) for d in menor]))
mayor = int(''.join([str(d) for d in mayor]))

diferencia = mayor - menor

print('{} - {} = {}'.format(mayor, menor, diferencia))
