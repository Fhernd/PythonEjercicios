# Ejercicio 59: Calcular la estatura (dada en pies y pulgadas) en centímetros.

# 1 ft = 30.48 cm
# 1 " = 2.54 cm

print('Escriba su estatura (ft y pulgadas): ')
pies = float(input('Pies: '))
pulgadas = float(input('Pulgadas: '))

cm = pies * 30.48
cm += pulgadas * 2.54

print('Su estatura es: {} cm'.format(cm))
