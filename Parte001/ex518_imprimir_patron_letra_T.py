# Ejercicio 518: Imprimir un patrón de asteriscos para representar la letra T mayúscula.

#  *****                                                                  
#    *                                                                    
#    *                                                                    
#    *                                                                    
#    *                                                                    
#    *                                                                    
#    *  

for i in range(7):
    for j in range(7):
        if i == 0 and 1 <= j <= 5:
            print('*', end='')
        elif i > 0 and j == 3:
            print('*', end='')
        else:
            print(' ', end='')
    print()
