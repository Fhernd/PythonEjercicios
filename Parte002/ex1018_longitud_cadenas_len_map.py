# Ejercicio 1018: Obtener la longitud de cada cadena de una lista con la función map().

nombres = ['Alexander', 'Diana', 'Luisa', 'Pedro', 'Fabián', 'Sebastián', 'Deisy']

# [9, 5, 5, 5, 6, 9, 5]

longitudes = list(map(len, nombres))
print(longitudes)
