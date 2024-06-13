# Ejercicio 515: Imprimir un patrón de asteriscos para representar la letra R mayúscula.

#  ****                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  ****                                                                   
#  * *                                                                    
#  *  *                                                                   
#  *   *

for i in range(7):
    for j in range(7):
        if (i == 0 or i == 3) and (1 <= j <= 4):
            print('*', end='')
        elif (i == 1 or i == 2) and (j == 1 or j == 5):
            print('*', end='')
        elif i == 4 and (j == 1 or j == 3):
            print('*', end='')
        elif i == 5 and (j == 1 or j == 4):
            print('*', end='')
        elif i == 6 and (j == 1 or j == 5):
            print('*', end='')
        else:
            print(' ', end='')
    print()
