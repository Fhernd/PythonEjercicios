# Ejercicio 851: Extraer la fecha desde una dirección Web (URL) con una expresión regular.

import re

# https://ortizol.blogspot.com/2020/06/20/python-ejercicio-849-reemplazar-el.html

def extraer_fecha_url(url):
    patron = r'/(\d{4})/(\d{2})/(\d{2})/'

    return re.findall(patron, url)


direccion_web = 'https://ortizol.blogspot.com/2020/06/20/python-ejercicio-849-reemplazar-el.html'

fecha = extraer_fecha_url(direccion_web)

print(fecha[0])
