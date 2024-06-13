# Ejercicio 1064: HackerRank Diseñador de puertas para la empresa del señor Vincent.

# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

# Mat size must be X. ( is an odd natural number, and  is  times .)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.

# ...

def generate_design(n, m):
    n = (n - 1) // 2
    columns = (m - 1) // 2
    rows = []
    
    for i in range(n):
        row = ['-' for _ in range(columns)]
        
        dots = 1 + i * 2
        j = 1
        
        while j <= (dots + i):
            row[j - 1] = '|' if j % 3 == 0 else '.'
            j += 1
        
        row = ''.join(row[::-1]) + '|' + ''.join(row)
        print(row)
        rows.append(row)
    
    print('{:-^{columns}}'.format('WELCOME', columns=m))
    
    for r in rows[::-1]:
        print(r)

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    
    generate_design(n, m)

