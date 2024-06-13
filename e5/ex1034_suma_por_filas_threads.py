# Ejercicio 1034: Usar threads para sumar los valores de cada fila de una matriz.

from threading import Thread

def sumar_fila(numeros, resultado):
    suma = 0

    for n in numeros:
        suma += n
    
    resultado.append(suma)


if __name__ == '__main__':
    matriz = [
        list(range(1, 1000)),
        list(range(1000, 2000)),
        list(range(2000, 3000)),
        list(range(3000, 4000)),
        list(range(4000, 5000)),
    ]

    threads = []
    sumas = []
    for f in matriz:
        threads.append(Thread(target=sumar_fila, args=(f, sumas)))
    
    for t in threads:
        t.start()
    
    for t in threads:
        t.join()
    
    suma = sum(sumas)
    print('La suma de todos los valores de la matriz es igual a:', suma)
