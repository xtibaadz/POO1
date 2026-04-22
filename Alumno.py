class Alumno:
    def __init__(self, nombre : str,edad : int, matricula: str):
        self.nombre = nombre
        self.edad = edad
        self.matricula = matricula

    def presentarse(self) -> str:
        return f"Hola, soy {self.nombre}, tengo {self.edad}, años y mi matricula es {self.matricula}."
    
if __name__ == "__main__":
    Alumno1 = Alumno("Julian", 20, "A1120")
    Alumno2 = Alumno("Andres", 12, "A1121")

    print(Alumno1.presentarse())
    print(Alumno2.presentarse())

if __name__ == "__main__":
    Juan = Alumno("Juan", 29, "A1122")
    print(Juan.presentarse())