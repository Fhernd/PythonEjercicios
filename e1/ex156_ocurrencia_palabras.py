# Ejercicio 156: Contar el número de ocurrencias de palabras en una frase o párrafo.

frase = """
Crimen y castigo ​(en ruso: Преступле́ние и наказа́ние, romanización: Prestupléniye i nakazániye) es una novela de carácter psicológico escrita por el autor ruso Fiódor Dostoievski. Fue publicada por primera vez en la revista El mensajero ruso, en 1866, en doce partes, y publicada después como novela.2​3​ Junto con Guerra y paz de León Tolstói, se considera que la novela es una de las más influyentes e internacionales de la literatura rusa.4​ Asimismo, los diálogos mantenidos entre el protagonista, Raskólnikov, y el inspector de policía, son considerados por algunos autores, como el prestigioso literato Stefan Zweig, una de las cimas de la literatura universal.

La historia narra la vida de Rodión Raskólnikov, un estudiante en la capital de la Rusia Imperial, San Petersburgo. Este joven se ve obligado a suspender sus estudios por la miseria en la cual se ve envuelto, a pesar de los esfuerzos realizados por su madre Pulqueria y su hermana Dunia para enviarle dinero. Necesitado de financiación para pagar sus gastos, había recurrido a una anciana prestamista vil y egoísta, en cuya casa empeña algunos objetos de valor.
"""

palabras = frase.split(' ')

frecuencia_palabras = [palabras.count(p) for p in palabras]

print('Frase:\n%s\n' % frase)
print('Ocurrencias palabrass: ', frecuencia_palabras)

print()

print(str(list(zip(palabras, frecuencia_palabras))))
