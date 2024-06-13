# Ejercicio 987: Obtener las ternas en el rango 1 a 1000 que forman triángulos rectángulos.

# cateto adyacente (a)
# cateto opuesto (b)
# hipotenusa (c)

# a ^ 2 + b ^ 2 = c ^ 2

ternas = []

for a in range(1, 1001):
    for b in range(1, 1001):
        for c in range(1, 1001):
            if a**2 + b**2 == c**2:
                ternas.append((a, b, c))

print('Cantidad de ternas:', len(ternas))

for t in ternas:
    print(t)
