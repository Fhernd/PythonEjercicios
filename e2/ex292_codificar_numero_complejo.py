# Ejercicio 292: Codificar un número complejo como datos en formato JSON usando dumps.

import json

def codificar_numero_complejo(complejo):
    if isinstance(complejo, complex):
        return [complejo.real, complejo.imag]
    else:
        raise TypeError('{} el valor no puede ser convertido a complejo'.format(repr(complejo)))


numero_complejo = 3 + 6j
complejo_json = json.dumps(numero_complejo, default=codificar_numero_complejo)

print(complejo_json)
