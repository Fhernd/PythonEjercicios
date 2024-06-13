# Ejercicio 219: Uso de la función format_map de la clase str.

datos = {'nombre': 'Edward Ortiz', 'email': 'edward@mail.com'}

resultado = 'Su nombre es: {nombre}. Su correo-e es: {email}'.format_map(datos)

print(resultado)
