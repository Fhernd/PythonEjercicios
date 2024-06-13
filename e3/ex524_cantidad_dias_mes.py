# Ejercicio 524: Determinar la cantidad de días de un mes ingresado por el usuario.

def cantidad_dias(mes):
    if mes.lower() in ('enero', 'marzo', 'julio', 'agosto', 'octubre', 'diciembre'):
        return '31'
    elif mes.lower() == 'febrero':
        return '28/29'
    else:
        return '30'


nombre_mes = input('Ingrese el nombre del mes: ')

print(cantidad_dias(nombre_mes))
