from string import ascii_lowercase, ascii_uppercase, digits


def sort_text(text):
    if text.isalnum():
        minusculas = list(filter(lambda c: c in ascii_lowercase, text))
        mayusculas = list(filter(lambda c: c in ascii_uppercase, text))
        digitos = list(filter(lambda c: c in digits, text))
        
        minusculas = ''.join(sorted(minusculas))
        mayusculas = ''.join(sorted(mayusculas))
        digitos = list(map(int, digitos))
        
        impares = sorted(list(filter(lambda n: n % 2 == 1, digitos)))
        pares = sorted(list(filter(lambda n: n % 2 == 0, digitos)))
        
        impares = ''.join(str(i) for i in impares)
        pares = ''.join(str(i) for i in pares)
        
        return minusculas + mayusculas + impares + pares
    
    return ''

    
if __name__ == '__main__':
    s = input()
    
    print(sort_text(s))
