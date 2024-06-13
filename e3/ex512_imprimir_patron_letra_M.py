# Ejercicio 512: Imprimir un patrón de asteriscos para representar la letra M mayúscula.

#   *       *                                                             
#   *       *                                                             
#   * *   * *                                                             
#   *   *   *                                                             
#   *       *                                                             
#   *       *                                                             
#   *       *

for i in range(7):
    for j in range(12):
        if (i == 0 or i == 1 or 4 <= i <= 6) and (j == 1 or j == 11):
            print('*', end='')
        elif i == 2 and (j == 1 or j == 3 or j == 9 or j == 11):
            print('*', end='')
        elif i == 3 and (j == 1 or j == 6 or j == 11):
            print('*', end='')
        else:
            print(' ', end='')
    print()
