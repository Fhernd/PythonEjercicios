# Ejercicio 160: Mostrar el listado de todos los módulos instalados localmente.

import pkg_resources

modulos_instalados = pkg_resources.working_set

modulos_instalados = sorted(["%s==%s" % (i.key, i.version) for i in modulos_instalados])

for m in modulos_instalados:
    print(m)
