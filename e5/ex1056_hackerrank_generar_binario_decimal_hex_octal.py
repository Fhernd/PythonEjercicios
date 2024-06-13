# Ejercicio 1056: HackerRank Generar números binarios, octales, hexadecimales, y decimales formateados.

# Given an integer, , print the following values for each integer  from  to :

# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary
# The four values must be printed on a single line in the order specified above for each  from  to . Each value should be space-padded to match the width of the binary value of .

# ...

def print_formatted(number):
    binary = bin(number)[2:]
    width = len(binary)
    
    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]
        
        print(decimal.rjust(width, ' ') + ' ' + octal.rjust(width, ' ') + ' ' + hexadecimal.rjust(width, ' ') + ' ' + binary.rjust(width, ' '))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
