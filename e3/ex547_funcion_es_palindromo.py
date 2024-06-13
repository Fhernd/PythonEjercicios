# Ejercicio 547: Crear una función para determinar si una cadena es palíndromo.

# ana
# madam

def es_palindromo(cadena):
    posicion_izquierda = 0
    posicion_derecha = len(cadena) - 1

    while posicion_derecha >= posicion_izquierda:
        if not cadena[posicion_izquierda] == cadena[posicion_derecha]:
            return False
        
        posicion_izquierda += 1
        posicion_derecha -= 1
    
    return True

print(es_palindromo('ana'))
print(es_palindromo('madam'))
print(es_palindromo('oso'))
print(es_palindromo('lateleletal'))
print(es_palindromo('python'))
