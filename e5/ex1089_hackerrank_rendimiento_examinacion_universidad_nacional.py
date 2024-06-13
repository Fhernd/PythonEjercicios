# Ejercicio 1089: HackerRank Cómputo rendimiento N estudiantes de la Universidad Nacional.

# Task

# The National University conducts an examination of  students in  subjects.
# Your task is to compute the average scores of each student.

# ...

if __name__ == '__main__':
    n, x = tuple(map(int, input().split()))
    
    scores = []
    for _ in range(x):
        scores.append(tuple(map(float, input().split())))
    
    result = list(zip(*scores))
    
    for r in result:
        average = sum(r) / len(r)
        print(average)
