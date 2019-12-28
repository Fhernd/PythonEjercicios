# Ejercicio 195: Encontrar la palabra más frecuente y la más larga de un texto dado.

from collections import Counter

texto = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec condimentum ipsum sit amet interdum pretium. Ut auctor magna ac elit molestie aliquet. Nulla quis nisl quam. Suspendisse nec blandit odio. Nulla purus neque, rhoncus quis ultricies vel, faucibus non turpis. Quisque eget tincidunt dolor. Maecenas sollicitudin tempor blandit. Donec tempus lectus sed nunc commodo elementum. Suspendisse volutpat felis vitae sapien iaculis, non tempus lectus laoreet. Maecenas id leo at ligula vehicula iaculis. Fusce ultrices vitae odio eget mattis. Aliquam auctor mattis ex ac tincidunt. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.'

palabras = texto.split()

contador = Counter(palabras)

palabra_frecuente = contador.most_common()[0][0]

print(contador.most_common())

print('Palabra más frecuente: %s' % palabra_frecuente)


def palabra_mas_larga(palabras):
    palabra = ''

    for p in palabras:
        if len(p) > len(palabra):
            palabra = p
    
    return palabra


print('La palabra más extensa es: %s' % palabra_mas_larga(palabras))
