# Ejercicio 858: Reemplazar todas las coincidencias el punto, la coma y el punto y coma por dos puntos (:).

import re

parrafo = 'Historia del Siglo XX. En el siglo pasado se inventaron diferentes dispositivos para el progreso de la humanidad. Uno de los inventos más sobresalientes es el computador. Esta invención cambió el mundo en Siglo XX: la economía, las relaciones humanas, la política, la educación y otros aspectos relevantes. El Siglo XX será recordado como un hito en la historia de la humanidad; una nueva perspectiva del mundo.'

patron = '[.,;]'

resultado = re.sub(patron, ':', parrafo)

print(resultado)
