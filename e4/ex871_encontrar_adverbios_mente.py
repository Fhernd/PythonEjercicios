# Ejercicio 871: Encontrar los adverbios terminados en -mente e identificar su posición.

import re

frase = 'Hoy principalmente me he dedicado a subir vídeos al canal de YouTube. Hay un motivo implícito en lo institivo que me impulsa a hacer esto a diario, incansablemente. Lo mejor es aprender a diario... aprender constamente.'

patron = r'\w+mente'

for c in re.finditer(patron, frase):
    print('%s: %d-%d' % (c.group(0), c.start(), c.end()))
