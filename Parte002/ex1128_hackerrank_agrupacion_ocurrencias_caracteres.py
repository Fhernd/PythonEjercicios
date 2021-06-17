# Ejercicio 1128: HackerRank Agrupación de ocurrencias consecutivas con la función groupby().

# In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . 
# To read more about this function, Check this out .

# You are given a string . Suppose a character '' occurs consecutively  times in the string. 
# Replace these consecutive occurrences of the character '' with  in the string.

# For a better understanding of the problem, check the explanation.

from itertools import groupby

if __name__ == '__main__':
    s = input()
    
    agrupacion = groupby(s)
    
    for a in agrupacion:
        ocurrencia = tuple(a[1])
        resultado = (len(ocurrencia), int(ocurrencia[0]))
        print(resultado, end=' ')
