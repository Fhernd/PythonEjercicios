# Ejercicio 676: Crear una función para obtener la fecha del último martes.

from datetime import date, timedelta

def fecha_ultimo_martes():
    hoy = date.today()
    dias = (hoy.weekday() - 1) % 7
    ultimo_martes = hoy - timedelta(days=dias)
    return ultimo_martes

resultado = fecha_ultimo_martes()
print('Fecha último martes:', resultado)
