# Ejercicio 528: Determinar la estación meteorológica del año a partir del nombre del mes.

def estacion_meteorologica(mes):
    if mes.lower() in ('enero', 'febrero', 'marzo'):
        return 'Invierno'
    elif mes.lower() in ('abril', 'mayo', 'junio'):
        return 'Primavera'
    elif mes.lower() in ('julio', 'agosto', 'septiembre'):
        return 'Verano'
    else:
        return 'Otoño'


mes = 'Enero'
print(estacion_meteorologica(mes))
mes = 'julio'
print(estacion_meteorologica(mes))
mes = 'Noviembre'
print(estacion_meteorologica(mes))
mes = 'abril'
print(estacion_meteorologica(mes))
