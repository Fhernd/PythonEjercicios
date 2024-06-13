# Ejercicio 513: Imprimir un patrón de asteriscos para representar la letra O mayúscula.

#   ***                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#   *** 

for i in range(7):
    for j in range(7):
        if (i == 0 or i == 6) and 2 <= j <= 4:
            print('*', end='')
        elif 1 <= i <= 5 and (j == 1 or j == 5):
            print('*', end='')
        else:
            print(' ', end='')
    print()
