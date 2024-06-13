# Ejercicio 510: Imprimir un patrón de asteriscos para representar la letra G mayúscula.

#   ***                                                                   
#  *   *                                                                  
#  *                                                                      
#  * ***                                                                  
#  *   *                                                                  
#  *   *                                                                  
#   *** 

for i in range(7):
    for j in range(7):
        if (i == 0 or i == 6) and 2 <= j <= 4:
            print('*', end='')
        elif (i == 1 or i == 4 or i == 5) and (j== 1 or j == 5):
            print('*', end='')
        elif i == 2 and j == 1:
            print('*', end='')
        elif i == 3 and (j == 1 or 3 <= j <= 5):
            print('*', end='')
        else:
            print(' ', end='')
    print()
