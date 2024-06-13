# Ejercicio 521: Imprimir un patrón de asteriscos para representar la letra Z mayúscula.

# *******                                                                 
#      *                                                                  
#     *                                                                   
#    *                                                                    
#   *                                                                     
#  *                                                                      
# *******

for i in range(7):
    for j in range(9):
        if (i == 0 or i == 6) and (1 <= j <= 7):
            print('*', end='')
        elif i == 1 and j == 6:
            print('*', end='')
        elif i == 2 and j == 5:
            print('*', end='')
        elif i == 3 and j == 4:
            print('*', end='')
        elif i == 4 and j == 3:
            print('*', end='')
        elif i == 5 and j == 2:
            print('*', end='')
        else:
            print(' ', end='')
    print()
