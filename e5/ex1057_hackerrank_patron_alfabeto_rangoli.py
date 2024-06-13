# Ejercicio 1057: HackerRank Generar patrón del alfabeto Rangoli según un tamaño N dado.

# You are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)

# Different sizes of alphabet rangoli are shown below:

# #size 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

# #size 5

# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

# ...

from string import ascii_lowercase

def print_rangoli(size):
    abc = ascii_lowercase[:size][::-1]
    rangoli_matrix = []
    
    for i in range(size):
        letters = abc[:i+1][::-1]
        row = []
        k = 0
        
        for j in range(size * 2 - 1):
            if k < len(letters) and j % 2 == 0:
                row.append(letters[k])
                k += 1
            else:
                row.append('-')
        
        row = ''.join(row[::-1]) + ''.join(row[1:])
        print(row)
        rangoli_matrix.append(row)
    
    rangoli_matrix.pop()
    for r in rangoli_matrix[::-1]:
        print(r)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
