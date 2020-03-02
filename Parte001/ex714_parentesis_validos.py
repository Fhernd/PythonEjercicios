# Ejercicio 714: Crear una función para comprobar si una cadena de paréntesis es válida.

# Análisis:
# '()[]{}' => True
# '()[]{}(' => False
# '(){][}' => False

def cadena_parentesis_valida(cadena):
    pila = []
    parentesis = {'{': '}', '(': ')', '[': ']'}

    for c in cadena:
        if c in parentesis:
            pila.append(c)
        elif len(pila) == 0 or c != parentesis[pila.pop()]:
            return False
    
    return len(pila) == 0


print(cadena_parentesis_valida('()[]{}'))
print(cadena_parentesis_valida('()[]{}('))
print(cadena_parentesis_valida('((){][}'))
