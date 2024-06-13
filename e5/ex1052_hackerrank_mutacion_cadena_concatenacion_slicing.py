# Ejercicio 1052: HackerRank Mutación de cadenas de caracteres usando concatenación y slicing.

# We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).

# Let's try to understand this with an example.

# You are given an immutable string, and you want to make changes to it.

# Example

# >>> string = "abracadabra"
# You can access an index by:

# >>> print string[5]
# a
# What if you would like to assign a value?

# >>> string[5] = 'k' 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment
# How would you approach this?

# One solution is to convert the string to a list and then change the value.
# Example

# >>> string = "abracadabra"
# >>> l = list(string)
# >>> l[5] = 'k'
# >>> string = ''.join(l)
# >>> print string
# abrackdabra
# Another approach is to slice the string and join it back.
# Example

# >>> string = string[:5] + "k" + string[6:]
# >>> print string
# abrackdabra

# ...

def mutate_string(string, position, character):
    result = string[:position] + character + string[position + 1:]
    
    return result

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
