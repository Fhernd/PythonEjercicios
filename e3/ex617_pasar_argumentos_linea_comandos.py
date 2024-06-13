# Ejercicio 617: Calcular el mayor de tres números pasados como argumentos desde la línea de comandos.

import sys

if len(sys.argv) == 4:
    numero_1 = sys.argv[1]
    numero_2 = sys.argv[2]
    numero_3 = sys.argv[3]

    if numero_1.isnumeric() and numero_2.isnumeric() and numero_3.isnumeric():
        mayor = max(int(numero_1), int(numero_2), int(numero_3))

        print('El número mayor es: {}'.format(mayor))
    else:
        print('Los valores deben ser de tipo numérico.')
else:
    print('Uso: <valor_1> <valor_2> <valor_3>')
    sys.exit(1)
