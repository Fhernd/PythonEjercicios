# Ejercicio 139: Validar si una dirección IP dada es válida.

import socket

def ip_valida(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False


print(ip_valida('127.0.0.1'))
print(ip_valida('192.168.0.1'))
print(ip_valida('192.168.0.1024'))
print(ip_valida('192.168.0.24.7'))
