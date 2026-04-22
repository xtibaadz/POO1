class Categorizar_Motos:
    def __init__(self, marca: str, color: str, matricula: str, modelo: int):
        self.marca = marca
        self.color = color
        self.matricula = matricula
        self.modelo = modelo

    def clasificar_tipo(self) -> str:
        if self.modelo < 3:
            return "Moto"
        elif self.modelo < 5:
            return "Cuatrimoto"
        else:
            return "Can-AM"
        
    def presentar_moto(self) -> str:
        categoria = self.clasificar_tipo()




    
        return f"Hola, tengo una {categoria},marca {self.marca}, clor {self.color} con matricula {self.matricula} y modelo {self.modelo}."

moto1 = Categorizar_Motos("Yamaha", "Gris", "PBB-21H", 2)

print(moto1.presentar_moto())