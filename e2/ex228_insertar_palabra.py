# Ejercicio 228: Insertar una palabra en una posición específica de una cadena.

# Solución:

# "Python 3.8.0" => "Python versión 3.8.0"

def insertar_texto(cadena, texto, posicion):
    if posicion <= len(cadena):
        izquierda = cadena[:posicion]
        derecha = cadena[posicion + 1:]

        return '{} {} {}'.format(izquierda, texto, derecha)
    else:
        raise ValueError('La posición donde se quiere insertar el texto no existe.')


cadena = 'Python 3.8.0'
texto = 'versión'
posicion = 6

print(insertar_texto(cadena, texto, posicion))
