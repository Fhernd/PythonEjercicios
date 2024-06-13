# Ejercicio 104: Obtener el ID de usuario, el ID de grupo, y grupos complementarios en Linux.

import os

print('El ID de usuario es: %d' % os.geteuid())
print('El ID de grupo es: %d' % os.getegid())
print('Los IDs de grupos complementarios son: {}'.format(str(os.getgroups())))
