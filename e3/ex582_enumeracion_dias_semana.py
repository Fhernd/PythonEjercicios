# Ejercicio 582: Crear una enumeración para representar los nombres de los días de la semana.

from enum import Enum

class Semana(Enum):
    Domingo = 1
    Lunes = 2
    Martes = 3
    Miércoles = 4
    Jueves = 5
    Viernes = 6
    Sabado = 7


domingo = Semana.Domingo
print(domingo)

numero_dia = 7
