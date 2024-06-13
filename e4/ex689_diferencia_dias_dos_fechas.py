# Ejercicio 689: Calcular la diferencia en días entre dos objetos fecha (date).

from datetime import date

def diferencia_dias(fecha_1, fecha_2):
    return (fecha_2 - fecha_1).days


ahora = date.today()
nacimiento_turin = date(1912, 6, 23)

resultado = diferencia_dias(nacimiento_turin, ahora)
print(resultado)

resultado = diferencia_dias(ahora, nacimiento_turin)
print(resultado)
