# Ejercicio 870: Extraer todas las direcciones de correo electrónico desde un texto.

import re

texto = """
Usuario 1: kronvold@verizon.net
Usuario 2: schumer@live.com
maneesh@outlook.com
richard@sbcglobal.net
daveewart@outlook.com
rfoley@aol.com
mjewell@mac.com
jgoerzen@comcast.net
raines@sbcglobal.net
marioph@outlook.com
jdhildeb@aol.com
janneh@optonline.net
"""

patron = r'[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}'

emails = re.findall(patron, texto)

print(emails)
