# Ejercicio 1048: HackerRank Definir una función para alternar entre minúsculas y mayúsculas.

# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

# For Example:

# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2

def swap_case(s):
    result = map(lambda c: c.lower() if c.isupper() else c.upper() , s)
    
    return ''.join(result)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
