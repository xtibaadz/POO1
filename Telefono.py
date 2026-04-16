class Telefono:
    def __init__(self, marca, sistema_operativo, ram, color, procesador):
        self.marca = marca
        self.sistema_operativo = sistema_operativo
        self.ram = ram
        self.color = color
        self.procesador = procesador

print(" ")
print("Primer Modelo De Telefono")
print(" ")

#1 Modelo
mi_telefono1 = Telefono("Iphone", "IOS", 12, "Verde", "Apple A15 Pro")
print(f"Marca: {mi_telefono1.marca}")
print(f"Sistema Operativo : {mi_telefono1.sistema_operativo}")
print(f"Ram: {mi_telefono1.ram}")
print(f"Color: {mi_telefono1.color}")
print(f"Procesador: {mi_telefono1.procesador}")


print(" ")
print("Siguiente Modelo De Telefono")
print(" ")

#2 Modelo
mi_telefono2 = Telefono("Iphone", "IOS", 12, "Titanium", "Apple A15 Pro")
print(f"Marca: {mi_telefono2.marca}")
print(f"Sistema Operativo : {mi_telefono2.sistema_operativo}")
print(f"Ram: {mi_telefono2.ram}")
print(f"Color: {mi_telefono2.color}")
print(f"Procesador: {mi_telefono2.procesador}")