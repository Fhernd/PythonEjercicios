# Ejercicio 680: Crear una función para sumar un mes a una fecha.

from datetime import date, timedelta
from calendar import monthrange

def cantidad_dias_mes(mes, agnio):
    """
    Obtiene la cantidad de días de un mes y año específicos.
    """
    return monthrange(agnio, mes)[1]

def sumar_mes_fecha(fecha):
    dias_mes = cantidad_dias_mes(fecha.month, fecha.year)
    resultado = fecha + timedelta(days=dias_mes)
    return resultado

fecha = date(2020, 12, 31)
resultado = sumar_mes_fecha(fecha)
print(resultado)
