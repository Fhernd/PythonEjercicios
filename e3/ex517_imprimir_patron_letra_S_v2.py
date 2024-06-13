# Ejercicio 517: Imprimir un patrón de asteriscos para representar la letra S mayúscula.

#  ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# oooo                                                                    
# oooo                                                                    
# oooo                                                                    
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
#              oooo                                                       
#              oooo                                                       
#              oooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo 

for i in range(15):
    for j in range(22):
        if i == 0 and 2 <= j <= 20:
            print('*', end='')
        elif (i == 1 or i == 2 or i == 6 or i == 7 or i == 8 or i == 12 or i == 13 or i == 14) and (1 <= j <= 19):
            print('*', end='')
        elif (3 <= i <= 5) and 1 <= j <= 4:
            print('*', end='')
        elif (9 <= i <= 11) and 16 <= j <= 19:
            print('*', end='')
        else:
            print(' ', end='')
    print()
