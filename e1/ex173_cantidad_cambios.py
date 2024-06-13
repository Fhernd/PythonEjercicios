# Ejercicio 173: Calcular la cantidad mínima de monedas para el cambio de una compra.

def calcular_cantidad_min_cambio(monto):
    nominaciones = [500, 200, 100, 50, 20, 10]
    monedas = 0

    for i in range(len(nominaciones)):
        nominacion = nominaciones[i]

        monedas += int(monto / nominacion)
        monto = int(monto % nominacion)
    
    return monedas


print(calcular_cantidad_min_cambio(1000))
print(calcular_cantidad_min_cambio(550))
print(calcular_cantidad_min_cambio(720))
