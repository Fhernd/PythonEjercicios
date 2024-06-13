# Ejercicio 655: Crear una función recursiva para calcular la suma armónica.

# 1 + 1/2 + 1/3 + 1/4 + ... + 1/n

def suma_armonica(n):
    if n < 2:
        return 1
    else:
        return 1/n + suma_armonica(n - 1)

resultado = suma_armonica(7)
print(resultado)
