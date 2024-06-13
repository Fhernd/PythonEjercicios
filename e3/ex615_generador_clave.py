# Ejercicio 615: Crear una función personalizada para la generación de contraseñas.

import string
import random

def generador_clave(tamagnio = 10, caracteres=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(caracteres) for _ in range(tamagnio))


print(generador_clave())
print(generador_clave(8))
print(generador_clave(8))
