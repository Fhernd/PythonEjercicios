# Ejercicio 1060: HackerRank Calcular las ganancias de la tienda de zapatos del señor Raghu.

# collections.Counter()
# A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.

from collections import Counter

def compute_total_money_earned(x, sizes, sizes_prices):
    total_earned = 0
    available_sizes = dict(Counter(sizes))
    
    for i in range(len(sizes_prices)):
        size_price = sizes_prices[i]
        size = size_price[0]
        price = size_price[1]
        
        if size in available_sizes:
            if available_sizes[size]:
                available_sizes[size] -= 1
                total_earned += price
    
    return total_earned

if __name__ == '__main__':
    x = int(input())
    sizes = list(map(int, input().split()))
    n = int(input())
    sizes_prices = []
    for _ in range(n):
        size_price = tuple(map(int, input().split()))
        
        sizes_prices.append(size_price)
    
    result = compute_total_money_earned(x, sizes, sizes_prices)
    
    print(result)

