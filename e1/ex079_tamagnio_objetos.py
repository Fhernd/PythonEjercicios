# Ejercicio 79: Obtener el tamaño en bytes de un objeto.

import sys

python = 'Python'
javascript = 'JavaScript'
java = 'Java'
csharp = 'C#'

print('La cadena %s ocupa %i bytes' % (python, sys.getsizeof(python)))
print('La cadena %s ocupa %i bytes' % (javascript, sys.getsizeof(javascript)))
print('La cadena %s ocupa %i bytes' % (java, sys.getsizeof(java)))
print('La cadena %s ocupa %i bytes' % (csharp, sys.getsizeof(csharp)))
