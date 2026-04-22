class Categorizar:
    def __init__(self, nombre : str,edad : int, matricula: str):
        self.nombre = nombre
        self.edad = edad
        self.matricula = matricula

    def clasificar_edad(self) -> str:
        if self.edad < 18:
            return "Menor de edad"
        elif self.edad < 30:
            return "Joven"
        elif self.edad < 60 :
            return "Señor/a"
        else:
            return"Adulto de la tercera edad"
        
    def presentarse(self) -> str:   
        categoria = self.clasificar_edad()
        return f"Hola, soy {self.nombre}, tengo {self.edad}, años y mi matricula es {self.matricula}y soy {categoria}."
    
Alumno1 = Categorizar("Julian", 20, "A1120",)
Alumno2 = Categorizar("Andres", 12, "A1121")
Alumno3 = Categorizar("Andrea", 69, "A1123")
Alumno4 = Categorizar("Nicole", 35, "A1124")

print(Alumno1.presentarse())
print(Alumno2.presentarse())
print(Alumno3.presentarse())
print(Alumno4.presentarse())
    
