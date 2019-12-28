# Ejercicio 273: Remover los ceros redundantes de una dirección IP.

# Solución:

# 192.168.001.072 => 192.168.1.72
# 192.168.070.13 => 192.168.70.13

def remover_ceros_redundantes(ip):
    nueva_ip = '.'.join([str(int(o)) for o in ip.split('.')])

    return nueva_ip


direccion_ip = '192.168.001.072'
print(direccion_ip)
print(remover_ceros_redundantes(direccion_ip))

print()

direccion_ip = '192.168.070.13'
print(direccion_ip)
print(remover_ceros_redundantes(direccion_ip))
