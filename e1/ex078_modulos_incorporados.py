# Ejercicio 78: Obtener un listado de los módulos incorporados disponibles.

import sys

nombres_modulos = sorted(sys.builtin_module_names)
nombres_modulos = ', '.join(nombres_modulos)

print(nombres_modulos)
