# Ejercicio 659: Crear una función para determinar si un año es bisiesto.

def es_bisiesto(agnio):
    if agnio % 400 == 0:
        return True
    elif agnio % 100 == 0:
        return False
    elif agnio % 4 == 0:
        return True
    else:
        return False

agnio = 2020
print('¿El año %i es bisiesto?: %s' % (agnio, es_bisiesto(agnio)))
agnio = 2013
print('¿El año %i es bisiesto?: %s' % (agnio, es_bisiesto(agnio)))
agnio = 2000
print('¿El año %i es bisiesto?: %s' % (agnio, es_bisiesto(agnio)))
