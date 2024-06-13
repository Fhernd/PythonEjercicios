# Ejercicio 514: Imprimir un patrón de asteriscos para representar la letra P mayúscula.

#  ****                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  ****                                                                   
#  *                                                                      
#  *                                                                      
#  *  

for i in range(7):
    for j in range(7):
        if (i == 0 or i == 3) and (1 <= j <= 4):
            print('*', end='')
        elif (i == 1 or i == 2) and (j == 1 or j == 5):
            print('*', end='')
        elif (4 <= i <= 6) and j == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
