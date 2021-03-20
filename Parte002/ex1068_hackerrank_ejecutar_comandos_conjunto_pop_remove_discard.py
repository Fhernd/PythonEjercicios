# Ejercicio 1068: HackerRank Ejecutar los comandos remove(), discard() y pop() sobre un conjunto (set).

# Task
# You have a non-empty set , and you have to execute  commands given in  lines.

# The commands will be pop, remove and discard.

# ...

def execute_commands(s, commands):
    for c in commands:
        parts = c.split()
        command = parts[0]
        
        if command == 'remove':
            value = int(parts[1])
            
            if value in s:
                s.remove(value)
        elif command == 'discard':
            value = int(parts[1])
            
            s.discard(value)
        elif command == 'pop':
            if len(s):
                s.pop()
    
    return sum(s)

if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    
    c = int(input())
    commands = []
    for i in range(c):
        commands.append(input())
    
    result = execute_commands(s, commands)
    
    print(result)
