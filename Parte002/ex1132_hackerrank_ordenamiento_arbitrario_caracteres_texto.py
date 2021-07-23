# Ejercicio 1132: HackerRank Crear ordenamiento arbitrario para los caracteres de un texto.

# You are given a string .
#  contains alphanumeric characters only.
#  Your task is to sort the string  in the following manner:

# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.

from string import ascii_lowercase, ascii_uppercase, digits


def sort_text(text):
    minusculas = list(set(text).intersection(set(ascii_lowercase)))
    mayusculas = list(set(text).intersection(set(ascii_uppercase)))
    digitos = list(set(text).intersection(set(digits)))
    
    minusculas = ''.join(sorted(minusculas))
    mayusculas = ''.join(sorted(mayusculas))
    digitos = list(map(int, digitos))
    
    impares = sorted(list(filter(lambda n: n % 2 == 1, digitos)))
    pares = sorted(list(filter(lambda n: n % 2 == 0, digitos)))
    
    impares = ''.join(str(i) for i in impares)
    pares = ''.join(str(i) for i in pares)
    
    return minusculas + mayusculas + impares + pares


if __name__ == '__main__':
    s = input()
    
    print(sort_text(s))
