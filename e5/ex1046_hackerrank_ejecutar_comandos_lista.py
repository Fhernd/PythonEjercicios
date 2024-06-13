# Ejercicio 1046: HackerRank Ejecutar comandos (métodos) arbitrarios de un objeto lista.

# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

# ...

if __name__ == '__main__':
    N = int(input())
    
    commands = []
    
    for i in range(N):
        commands.append(input())
    
    numbers = []
    
    for c in commands:
        parts = c.split()
        command = parts[0]
        
        if command == 'insert':
            index = int(parts[1])
            value = int(parts[2])
            
            numbers.insert(index, value)
        elif command == 'print':
            print(numbers)
        elif command == 'remove':
            value = int(parts[1])
            if value in numbers:
                numbers.remove(value)
        elif command == 'append':
            value = int(parts[1])
            numbers.append(value)
        elif command == 'sort':
            numbers.sort()
        elif command == 'pop':
            if len(numbers):
                numbers.pop()
        else:
            numbers.reverse()
