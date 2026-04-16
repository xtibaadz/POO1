class Auto:
    def __init__(self, marca, color,ruedas, modelo,placa):
        self.marca = marca
        self.color = color
        self.ruedas = ruedas
        self.modelo = modelo
        self.placa = placa


print(" ")
print("Primer Modelo De Carro")
print(" ")

#1 Modelo
mi_auto1 = Auto("Lamborgini", "Verde", 4, 2026, "UXT - 789")
print(f"Marca: {mi_auto1.marca}")
print(f"Color: {mi_auto1.color}")
print(f"Ruedas: {mi_auto1.ruedas}")
print(f"Modelo: {mi_auto1.modelo}")
print(f"Placa: {mi_auto1.placa}")

print(" ")
print("Siguiente Modelo De Carro")
print(" ")

#2 Modelo
mi_auto2 = Auto("Taxi", "Amarillo", 4, 2012, "PNG - 125")
print(f"Marca: {mi_auto2.marca}")
print(f"Color: {mi_auto2.color}")
print(f"Ruedas: {mi_auto2.ruedas}")
print(f"Modelo: {mi_auto2.modelo}")
print(f"Placa: {mi_auto2.placa}")

print(" ")
print("Siguiente Modelo De Carro")
print(" ")

#3 Modelo
mi_auto3 = Auto("Tesla", "Blanco", 4, 2028, "PBB - 125")
print(f"Marca: {mi_auto3.marca}")
print(f"Color: {mi_auto3.color}")
print(f"Ruedas: {mi_auto3.ruedas}")
print(f"Modelo: {mi_auto3.modelo}")
print(f"Placa: {mi_auto3.placa}")
