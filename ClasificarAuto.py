#Molde para crear los nuevos objetos ( Autos )
class Categorizar_Auto:
    def __init__(self, color: str, marca: str, matricula: str, modelo: int, tipo_vehiculo: int):
        self.color = color
        self.marca = marca
        self.matricula = matricula
        self.modelo = modelo
        self.tipo_vehiculo = tipo_vehiculo

# Categorizar por modelo ( Nuevo, Semi Nuevo, Viejo )

    def clasificar_modelo(self) -> str:
        if self.modelo < 1950:
            return "Auto Viejo"
        elif self.modelo < 1990:
            return "Auto Semi Nuevo"
        elif self.modelo < 2010:
            return "Auto Nuevo"
        else:
            return "Auto Moderno"

# Categorizar tipo de vehículo ( Moto, Carro, Camion )

    def clasificar_vehiculo(self) -> str:
        if self.tipo_vehiculo < 3:
            return "Moto"
        elif self.tipo_vehiculo < 5:
            return "Carro"
        else:
            return "Camion"

# Presentacion

    def presentar_carro(self) -> str:
        categoria = self.clasificar_modelo()
        tipo = self.clasificar_vehiculo()

        return f"KlK chamo, tengo un/a super {tipo}, color {self.color}, marca {self.marca}, modelo {self.modelo}, matrícula {self.matricula}. Es un {categoria}."


# Crear carros 

carro1 = Categorizar_Auto("Rojo", "Ferrari", "A1120", 2005, 4)
carro2 = Categorizar_Auto("Verde", "Lambo", "A1121", 2026, 2)
carro3 = Categorizar_Auto("Gris", "Mazda", "A1123", 1951, 4)
carro4 = Categorizar_Auto("Negro", "Mercedez", "A1124", 2007, 8)

# Imprimir carros

print(carro1.presentar_carro())
print(carro2.presentar_carro())
print(carro3.presentar_carro())
print(carro4.presentar_carro())