# Ejercicio 867: Extraer enlaces (URLs) desde un texto con una expresión regular.

import re

texto = 'Página oficial de Python (v. 3.8.0): https://www.python.org/. URL corta de este canal: http://bit.ly/2SiCmCJ'

patron = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

urls = re.findall(patron, texto)

for u in urls:
    print(u)
