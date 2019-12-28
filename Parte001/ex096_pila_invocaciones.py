# Ejercicio 96: Imprimir el estado de la pila de llamadas.

import traceback

def funcion():
    xyz()


def xyz():
    traceback.print_stack()


funcion()
