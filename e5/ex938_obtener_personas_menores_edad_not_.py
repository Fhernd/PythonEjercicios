# Ejercicio 938: Utilizar la función not_() para obtener las personas menores de edad desde una lista.

from operator import not_

class Estudiante:
    def __init__(self, codigo, nombre, carrera, edad):
        self.codigo = codigo
        self.nombre = nombre
        self.carrera = carrera
        self.edad = edad
    
    def __str__(self):
        return f'Código: {self.codigo} - Nombre: {self.nombre}'

estudiantes = [
    Estudiante(1001, 'Angela Burgos', 'Sistemas', 17),
    Estudiante(1002, 'Carlos Tovar', 'Civil', 19),
    Estudiante(1003, 'Fabián Artunduaga', 'Sistemas', 20),
    Estudiante(1004, 'Sonia García', 'Industrial', 16),
]

estudiantes_menores_edad = list(filter(lambda e: not_(e.edad >= 18), estudiantes))

for e in estudiantes_menores_edad:
    print(e)
