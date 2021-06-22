# Ejercicio 1130: HackerRank Encontrar todas las subcadenas que cumplan un formato dado.

# Consider the following:

# A string, , of length  where .
# An integer, , where  is a factor of .
# We can split  into  substrings where each subtring, , consists of a contiguous block of  characters in . 
# Then, use each  to create string  such that:

# ...

from collections import OrderedDict


def particionar_texto(text, k):
    return [text[i: i + k] for i in range(0, len(text), k)]


def merge_the_tools(string, k):
    # your code goes here
    particiones = particionar_texto(string, k)
    
    for p in particiones:
        print(''.join(OrderedDict.fromkeys(p)))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
