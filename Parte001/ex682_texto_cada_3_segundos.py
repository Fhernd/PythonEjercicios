# Ejercicio 682: Crear función para imprimir un texto específico cada 3 segundos.

import time

def imprimir_texto(texto, n, intervalo=3):
    for _ in range(n):
        print(texto)
        time.sleep(intervalo)

imprimir_texto('¡Python es tremendo!', 5)
