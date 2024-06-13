# Ejercicio 695: Calcular la edad en años a partir de la fecha de nacimiento.

from datetime import date

def calcular_edad_agnios(fecha_nacimiento):
    fecha_actual = date.today()
    resultado = fecha_actual.year - fecha_nacimiento.year
    resultado -= ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return resultado

fecha_nacimiento_turing = date(1912, 6, 23)
edad = calcular_edad_agnios(fecha_nacimiento_turing)

print(f'La edad de Turin es de {edad} años.')
