# Ejercicio 1072: HackerRank Operaciones que mutan o cambian un objeto conjunto (set).

# TASK
# You are given a set  and  number of other sets. These  number of sets have to perform some specific mutation
#  operations on set .

# Your task is to execute those operations and print the sum of elements from set .

if __name__ == '__main__':
    m = int(input())
    a = set(map(int, input().split()))
    
    n = int(input())
    
    operations = []
    
    for _ in range(n):
        command_quantity = input().split()
        command = command_quantity[0]
        quantity = int(command_quantity[1])
        numbers = set(map(int, input().split()))
        operations.append((command, quantity, numbers))
    
    print(operations)
