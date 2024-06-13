# Ejercicio 1050: HackerRank Generación de listas por comprensión para crear permutaciones.

# Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a 
# cuboid along with an integer . Print a list of all possible coordinates given by  on a 3D grid where the sum 
# of  is not equal to . Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.

# ...

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    matrix = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)]
    
    result = [r for r in matrix if sum(r) != n]
    
    print(result)
