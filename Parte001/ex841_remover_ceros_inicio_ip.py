# Ejercicio 841: Remover los ceros al inicio de cada octeto de una dirección IP.

import re

def remover_ceros_al_inicio(ip):
    patron = '\.[0]*'

    return re.sub(patron, '.', ip)

direccion_ip = '192.168.013.001' # 192.168.13.1
print(remover_ceros_al_inicio(direccion_ip))
