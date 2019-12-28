# Ejercicio 247: Justificar un valor numérico a la izquierda, centro y derecha de una cadena.

# Solución:

# 2050
# < : justifica a la izquierda
# ^ : justifica al centro

puntaje = 2050

print('Valor original de puntaje:', puntaje)
print('Puntaje justificado a la izquierda:')
print('{:<20}'.format(puntaje))
print('Puntaje justificado al centro:')
print('{:^20}'.format(puntaje))
print('Puntaje justificado a la derecha:')
print('{:20}'.format(puntaje))
