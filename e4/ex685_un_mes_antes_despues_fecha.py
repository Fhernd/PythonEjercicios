# Ejercicio 685: Generar las fechas de hace 30 días y después de 30 días a partir de la actual.

from datetime import date, timedelta

def generar_fechas_30_dias():
    fecha_actual = date.today()
    hace_30_dias = fecha_actual - timedelta(days=30)
    despues_30_dias = fecha_actual + timedelta(days=30)

    return hace_30_dias, fecha_actual, despues_30_dias


resultado = generar_fechas_30_dias()
print(resultado)
