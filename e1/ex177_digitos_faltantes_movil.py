# Ejercicio 177: Encontrar los dígitos faltantes en un número de teléfono móvil.

# 3112223333 => 0456789
# {1, 2, 3}
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} - {1, 2, 3} = {0, 4, 5, 6, 7, 8, 9}


def encontrar_digitos_faltantes(numero):
    if isinstance(numero, str):
        try:
            numero = int(numero)

            if numero > 0:
                
                digitos = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
                numero = {int(d) for d in str(numero)}

                digitos_faltantes = digitos.difference(numero)

                return digitos_faltantes
            else:
                raise ValueError('El número de teléfono debe ser positivo.')
        except:
            raise ValueError('El argumento no es un número')
    else:
        raise TypeError('El argumento no es de tipo cadena de caracteres.')


print(encontrar_digitos_faltantes('3112223333'))

# print(encontrar_digitos_faltantes('-3112223333'))

# print(encontrar_digitos_faltantes('3112223333a'))
