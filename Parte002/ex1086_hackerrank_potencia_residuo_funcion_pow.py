# Ejercicio 1086: HackerRank Usar la función incorporada pow() para la potencia y el residuo.

# Task
# You are given three integers: , , and , respectively. Print two lines.
# The first line should print the result of pow(a,b). The second line should print the result of pow(a,b,m).

# ...

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    m = int(input())
    
    result = pow(a, b)
    reminder = pow(a, b, m)
    
    print(result)
    print(reminder)
