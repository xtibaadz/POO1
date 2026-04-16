class Moto:
    def __init__(self, marca, color,ruedas, modelo,placa):
        self.marca = marca
        self.color = color
        self.ruedas = ruedas
        self.modelo = modelo
        self.placa = placa

print(" ")
print("Primer Modelo De Moto")
print(" ")

#1 Modelo
mi_moto1 = Moto("Ducati", "Rojo", 2, 2026, "PBB - 21H")
print(f"Marca: {mi_moto1.marca}")
print(f"Color: {mi_moto1.color}")
print(f"Ruedas: {mi_moto1.ruedas}")
print(f"Modelo: {mi_moto1.modelo}")
print(f"Placa: {mi_moto1.placa}")

print(" ")
print("Siguiente Modelo De Moto")
print(" ")

#2 Modelo
mi_moto2 = Moto("MT 09", "Negro", 2, 2026, "PBB - 21H")
print(f"Marca: {mi_moto2.marca}")
print(f"Color: {mi_moto2.color}")
print(f"Ruedas: {mi_moto2.ruedas}")
print(f"Modelo: {mi_moto2.modelo}")
print(f"Placa: {mi_moto2.placa}")

