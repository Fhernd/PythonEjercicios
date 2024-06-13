# Ejercicio 857: Reemplazar todas las coincidencias de un valor en una cadena de caracteres.

import re

parrafo = 'Historia del Siglo XX. En el siglo pasado se inventaron diferentes dispositivos para el progreso de la humanidad. Uno de los inventos más sobresalientes es el computador. Esta invención cambió el mundo en Siglo XX: la economía, las relaciones humanas, la política, la educación y otros aspectos relevantes. El Siglo XX será recordado como un hito en la historia de la humanidad.'

patron = 'XX'

resultado = re.sub(patron, '20', parrafo)

print(resultado)
