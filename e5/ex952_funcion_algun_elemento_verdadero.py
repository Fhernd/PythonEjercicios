# Ejercicio 952: Definir una función para validar si al menos un elemento de una colección es verdadero.

def algun_elemento_verdadero(datos):
    for d in datos:
        if d:
            return True
    
    return False


coleccion = ['123', True, (1, 2), ['John', 'Oliva', 'Juan'], {'a': 1}]
print(algun_elemento_verdadero(coleccion))  # True

print()

coleccion = ['', False, 0, not True, """""", '''''']
print(algun_elemento_verdadero(coleccion))  # False
