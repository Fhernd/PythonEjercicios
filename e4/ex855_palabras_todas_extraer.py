# Ejercicio 855: Encontrar todas las palabras que empiecen con las vocales a y e.

import re

extracto = "Loca ligeros pensamiento tierra que quemadas comida. Para las alegrísima latido desnudo convexa pero abrir. De lenta abeja del por de subía la despenada, quedo ansioso borrachos es la que y, tierra hombrecillo se resonancia quedo todo. Es la muerte los sillas borrando, pulso ojos deja mujer la. De de tierra nunca las de gustada sus diana hombrecillo, brooklyn resonancia llenando lenguas golondrina, la tierra heridas con es. De que cosas musgos me que pulso, con mujer y para ligeros donde la con pies repartiendo, ciudades queman es sus el plata. Bajo apariencia la el los la escaleras quedo, amor."

patron = r'\b[AaEe]\w+\b'

resultado = re.findall(patron, extracto)

for p in resultado:
    print(p)
