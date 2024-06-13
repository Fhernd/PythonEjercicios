# Ejercicio 1032: Usar la clase Thread del módulo threading para ejecutar dos tareas.

from threading import Thread

def cuadrados(n):
    for i in range(1, n + 1):
        print(f'{i} ^ 2 = {i**2}')


def cubo(n):
    for i in range(1, n + 1):
        print(f'{i} ^ 3 = {i**3}')


if __name__ == '__main__':
    t1 = Thread(target=cuadrados, args=(10,))
    t2 = Thread(target=cubo, args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('El programa ha finalizado')