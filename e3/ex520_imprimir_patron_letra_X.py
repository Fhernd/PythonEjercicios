# Ejercicio 520: Imprimir un patrón de asteriscos para representar la letra X mayúscula.

#  *   *                                                                  
#  *   *                                                                  
#   * *                                                                   
#    *                                                                    
#   * *                                                                   
#  *   *                                                                  
#  *   *

for i in range(7):
    for j in range(7):
        if (i == 0 or i == 1 or i == 5 or i == 6) and (j == 1 or j == 5):
            print('*', end='')
        elif (i == 2 or i == 4) and (j == 2 or j == 4):
            print('*', end='')
        elif i == 3 and j == 3:
            print('*', end='')
        else:
            print(' ', end='')
    
    print()
