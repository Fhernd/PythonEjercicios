# Ejercicio 1061: HackerRank Calcular la altura promedio de las plantas de la señora Williams.

# Task

# Now, let's use our knowledge of sets and help Mickey.

# Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

# Formula used:

# ...

def average(heights):
    heights = set(heights)
    length = len(heights)
    
    result = sum(heights) / length
    
    return result
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
