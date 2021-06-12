# Ejercicio 1127: HackerRank Multiplicar números racionales por medio de la función reduce() de functools.

# Given a list of rational numbers,find their product.

# Concept
# The reduce() function applies a function of two arguments cumulatively on a list of objects in 
# succession from left to right to reduce it to one value. Say you have a list, say [1,2,3] and 
# you have to find its sum.

from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda f1, f2: f1 * f2, fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
