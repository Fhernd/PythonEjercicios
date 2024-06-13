# Ejercicio 1102: HackerRank Generar matrices con ceros y unos usando la librería NumPy.

# Task

# You are given the shape of the array in the form of space-separated integers, each integer representing 
# the size of different dimensions, your task is to print an array of the given shape and integer 
# type using the tools numpy.zeros and numpy.ones.

# ...

import numpy

array = tuple(map(int, input().split()))

zeros = numpy.zeros(array, int)
ones = numpy.ones(array, int)

print(zeros)
print(ones)
