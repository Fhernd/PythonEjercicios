# Ejercicio 544: Crear una función para comprobar si un número dado es primo.

def es_primo(numero):
    if numero == 1:
        return False
    elif numero == 2:
        return True
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        
        return True


for i in range(1, 101):
    print(i, es_primo(i))
