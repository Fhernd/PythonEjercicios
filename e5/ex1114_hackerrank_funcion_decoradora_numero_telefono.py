# Ejercicio 1114: HackerRank 1/2 Usar una función decoradora para formatear números de teléfono.

# Task
# The first line of input contains an integer , the number of mobile phone numbers.
#  lines follow each containing a mobile number.

# ...

def wrapper(f):
    def fun(l):
        l = [p[-10:] for p in l]
        l = ['+91 ' + p[:5] + ' ' + p[-5:] for p in l]
        f(l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
