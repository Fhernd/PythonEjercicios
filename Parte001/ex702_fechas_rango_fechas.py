# Ejercicio 702: Crear una función para generar una lista de fechas en un rango específico.

from datetime import date, timedelta

def generar_rango_fechas(fecha_1, fecha_2):
    fechas = []
    dias = (fecha_2 - fecha_1).days + 1

    for i in range(dias):
        fechas.append(fecha_1 + timedelta(i))
    
    return fechas

inicio = date(2020, 2, 1)
fin = date(2020, 2, 15)

resultado = generar_rango_fechas(inicio, fin)

for f in resultado:
    print(f)
