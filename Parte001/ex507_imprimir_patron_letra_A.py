# Ejercicio 507: Imprimir un patrón de asteriscos para representar la letra A mayúscula.

#   ***                                                                                                         
#  *   *                                                                                                        
#  *   *                                                                                                        
#  *****                                                                                                        
#  *   *                                                                                                        
#  *   *                                                                                                        
#  *   * 

for i in range(0, 7):
    for j in range(0, 7):
        if (i == 0 and ( 2 <= j <= 4)):
            print('*', end='')
        elif (i == 1 or i == 2 or i >= 4) and (j == 1 or j == 5):
            print('*', end='')
        elif i == 3 and 1 <= j <= 5:
            print('*', end='')
        else:
            print(' ', end='')
    
    print()
