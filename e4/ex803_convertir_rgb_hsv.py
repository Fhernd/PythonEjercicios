# Ejercicio 802: Crear una función para convertir un color RGB en HSV.

def rgb_a_hsv(r, g, b):
    r = r / 255.0
    g = g / 255.0
    b = b / 255.0

    minimo = min(r, g, b)
    maximo = max(r, g, b)
    diferencia = maximo - minimo

    if minimo == maximo:
        h = 0
    elif maximo == r:
        h = (60 * ((g - b)/diferencia) + 360) % 360
    elif maximo == g:
        h = (60 * ((g - b)/diferencia) + 120) % 360
    elif maximo == b:
        h = (60 * ((g - b)/diferencia) + 240) % 360

    if maximo == 0:
        s = 0
    else:
        s = (diferencia / maximo) * 100
    
    v = maximo * 100

    return h, s, v


print(rgb_a_hsv(255, 0, 0))
print(rgb_a_hsv(255, 120, 30))
