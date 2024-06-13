# Ejercicio 67: Convertir kilopascales (kPa) en presión psi, mmHg, y atm.


def conversion_kilopascales(kpa):
    """
    Conversión de unidades de presión.
    """
    psi = kpa / 6.89475729
    mmhg = kpa * 760 / 101.325
    atm = kpa / 101.325

    return psi, mmhg, atm


kilopascales = float(input('Escriba la presión en kilopascales (kPa): '))

print(conversion_kilopascales(kilopascales))
