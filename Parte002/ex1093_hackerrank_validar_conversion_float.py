# Ejercicio 1093: HackerRank Validar la conversión de números de punto flotante (float).

# You are given a string .
# Your task is to verify that  is a floating point number.

# In this task, a valid float number must satisfy all of the following requirements:

#  Number can start with +, - or . symbol.
# For example:

# ...

def is_valid_float(case):
    try:
        if case == '0':
            return False
        
        float(case)
        
        return True
    except:
        return False

if __name__ == "__main__":
    t = int(input())
    cases = [input() for _ in range(t)]
    
    for c in cases:
        print(is_valid_float(c))
