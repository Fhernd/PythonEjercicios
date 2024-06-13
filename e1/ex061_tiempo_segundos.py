# Ejercicio 61: Convertir todas las unidades de tiempo en segundos.

dias = int(input('Escriba la cantidad de días: '))
horas = int(input('Escriba la cantidad de horas: '))
minutos = int(input('Escriba la cantidad de minutos: '))
segundos = int(input('Escriba la cantidad de segundos: '))

segundos += dias * 24 * 60 * 60
segundos += horas * 60 * 60
segundos += minutos * 60

print('La cantidad de segundos es igual: {}'.format(segundos))
