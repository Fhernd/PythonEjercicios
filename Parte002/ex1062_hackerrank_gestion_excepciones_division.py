# Ejercicio 1062: HackeRank Gestión de errores y excepciones al intentar dividir números.

# Task

# You are given two values  and .
# Perform integer division and print .

# Input Format

# The first line contains , the number of test cases.
# The next  lines each contain the space separated values of  and .

# ...

def try_divisions(data):
    for d in data:
        value_1 = d[0]
        value_2 = d[1]
        
        try:
            print(int(value_1) // int(value_2))
        except (ZeroDivisionError, ValueError) as e:
            print('Error Code:', e)

if __name__ == '__main__':
    t = int(input())
    data = []
    for _ in range(t):
        values = input().split()
        data.append(values)
    
    try_divisions(data)
