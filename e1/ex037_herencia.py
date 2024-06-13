# Ejercicio 37: Crear una jerarquía de herencia básica.

# Persona <- Estudiante


class Persona:
    def __init__(self, documento, nombre, correo):
        self.documento = documento
        self.nombre = nombre
        self.correo = correo


class Estudiante(Persona):
    def __init__(self, documento, nombre, correo, carnet, carrera):
        super().__init__(documento, nombre, correo)
        self.carnet = carnet
        self.carrera = carrera


german = Estudiante('123', 'Germán', 'german@mail.co', '987', 'Computación')

print(isinstance(german, Estudiante))
print(isinstance(german, Persona))
