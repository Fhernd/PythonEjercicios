# Ejercicio 1049: HackerRank Imprimir el nombre completo de una persona con una cadena de formato.

# You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

# Hello firstname lastname! You just delved into python.

# ...

def print_full_name(a, b):
    print(f'Hello {a} {b}! You just delved into python.')

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)