# Ejercicio 1065: HackeRank Ayudar la señorita Rupal a contar la cantidad de estampillas de su colección.

# Apply your knowledge of the .add() operation to help your friend Rupal.

# Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of  country stamps.

# Find the total number of distinct country stamps.

# ...

if __name__ == '__main__':
    n = int(input())
    countries = set([input() for _ in range(n)])
    
    print(len(countries))
