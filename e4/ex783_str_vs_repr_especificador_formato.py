# Ejercicio 783: Usar un especificador de formato para las representación formal (repr) e informal (str) de un objeto.

# str(): obtenemos la representación informal de un objeto.
# repr(): obtenemos la representación formal de un objeto.

class Persona:
    def __str__(self):
        return 'Persona'
    
    def __repr__(self):
        return 'Persona <Persona>'


p = Persona()

# Mecanismo tradicional con %s o %r:
print('%s - %r' % (p, p))

print()

# Nuevo mecanismo - Función format()
print('{0!s} - {0!r}'.format(p))
