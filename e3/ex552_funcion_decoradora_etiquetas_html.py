# Ejercicio 552: Crear funciones decoradoras para aplicar etiquetas HTML a un texto.

def negrita(fn):
    def envoltura():
        return f'<b>{fn()}</b>'
    
    return envoltura

def cursiva(fn):
    def envoltura():
        return f'<i>{fn()}</i>'
    
    return envoltura

def subrayado(fn):
    def envoltura():
        return f'<u>{fn()}</u>'
    
    return envoltura

@negrita
@cursiva
@subrayado
def aplicar_etiquetas():
    return 'Python'


resultado = aplicar_etiquetas()
print(resultado)
