# Ejercicio 1058: HackerRank Usar el módulo textwrap para ajuste de texto según un ancho dado.

# You are given a string  and width .
# Your task is to wrap the string into a paragraph of width .

# ...

import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    
    return '\n'.join(wrapper.wrap(text=string))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
