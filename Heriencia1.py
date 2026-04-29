print( )
print("Presentacion Estudiante")
print( )

class Estudiante:
    def __init__(self, nombre: str, apellido: str, grado: int, email: str):
        self.nombre = nombre
        self.apellido = apellido
        self.grado = grado
        self.email = email

    def presentacion_estudiante(self):
        return f"Soy el estudiante {self.nombre} {self.apellido}, grado {self.grado}, correo {self.email}"
    
objEstudiante = Estudiante("Julian", "Aguilera", 9, "tbdz@gmail.com")

print(objEstudiante.presentacion_estudiante())  

#Profesor hereda de Estudiante

print( )
print("Turno Profesor")
print( )

class Profesor(Estudiante):
    def __init__(self, nombre: str, apellido: str, grado: int, email: str, titulo: str, rango: str):
        
        super().__init__(nombre, apellido, grado, email)  #Hereda del padre
        
        self.titulo = titulo
        self.rango = rango

    def presentacion_profesor(self):
        return f"Soy el profesor {self.nombre} {self.apellido}, título {self.titulo}, rango {self.rango}"
        

# Crear objeto Profesor

objProfesor1 = Profesor("Julian", "Aguilera", 9, "tbdz@gmail.com", "Ing Sistemas", "Administrativo")

print(objProfesor1.presentacion_profesor())

print( )
print("Turno Empleado")
print( )

#Empleado hereda de Estudiante

class Empleado(Estudiante):
    def __init__(self, nombre, apellido, grado, email, trabajo, horario):

        super().__init__(nombre, apellido, grado, email)

        self.trabajo = trabajo
        self.horario = horario

    def presentacion_empleado(self):
        return f"Soy el empleado {self.nombre} {self.apellido}, email {self.email}, con grado {self.grado} asignado del trabajo {self.trabajo} y mi horario es {self.horario}."

objEmpleado1 = Empleado("Anthonio", "Aguilera", "tbdzzz@gmail.com", "Administrativo", "Cocinero", "Nocturno")   

print(objEmpleado1.presentacion_empleado())