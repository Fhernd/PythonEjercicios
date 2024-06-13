# Ejercicio 268: Mover el espacio de una cadena de caracteres al principio.

# Análisis:

# 'https  :/ /  www.python . org' => '       https://www.python.org'

def mover_espacio_al_frente(cadena):
    contador = cadena.count(' ')
    cadena = cadena.replace(' ', '')

    return ' ' * contador + cadena


texto = 'https  :/ /  www.python . org'

print(texto)
print(mover_espacio_al_frente(texto))
