# Ejercicio 95: Comprobar si una cadena de caracteres representa un número.


def es_numerico(cadena):
    try:
        float(cadena)
        return True
    except (TypeError, ValueError):
        return False


cadena = '2.7182'

print(es_numerico(cadena))

cadena = '3.1415ab'

print(es_numerico(cadena))

cadena = (5.3, 7.9)

print(es_numerico(cadena))
