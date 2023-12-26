# Ejercicio 1: Mostrar la versión actual de Python instalada.

import sys

def mostrar_version():
    print("Versión de Python instalada:")
    print(sys.version)
    print("\nInformación detallada:")
    print(sys.version_info)

if __name__ == "__main__":
    mostrar_version()
