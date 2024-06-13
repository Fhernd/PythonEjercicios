# Ejercicio 535: Construir un patrón de números por medio de un ciclo for anidado.

# 1                                                                                                             
# 22                                                                                                            
# 333                                                                                                           
# 4444                                                                                                          
# 55555                                                                                                         
# 666666                                                                                                        
# 7777777                                                                                                       
# 88888888                                                                                                      
# 999999999  

for n in range(1, 10):
    # for x in range(n):
    #     print(n, end='')
    print(str(n) * n)
