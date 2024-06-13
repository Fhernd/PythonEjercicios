# Ejercicio 863: Extraer todas las palabras que se hallen entre comillas dobles desde una cadena de caracteres.

import re

texto = '"Python", "JavaScript", "C++", "Java"'

patron = r'"(.*?)"'

lenguajes = re.findall(patron, texto)

print(lenguajes)

print()

for l in lenguajes:
    print(l)
