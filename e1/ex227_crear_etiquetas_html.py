# Ejercicio 227: Diseñar e implementar una función para crear etiquetas HTML.

# Solución:

# <tag>CONTENIDO</tag>
# <span>Texto...</span>
# <p>Texto...</p>


def crear_etiqueta(etiqueta, contenido):
    return '<%s>%s</%s>' % (etiqueta, contenido, etiqueta)


print(crear_etiqueta('span', 'Python es tremendo'))
print(crear_etiqueta('p', 'Python es tremendo. Python es un lenguaje de programación.'))
