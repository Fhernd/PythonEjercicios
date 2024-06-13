# Ejercicio 875: Remover el contenido textual que se encuentre dentro de paréntesis.

import re

texto = 'Python (v. 3.8.0) - Java (14) - C# (7) - JavaScript (ES6)'

patron = r'\([^)]+\)'

resultado = re.sub(patron, '', texto)

print(resultado)

resultado = re.sub(r'\s+', ' ', resultado)

print(resultado)
