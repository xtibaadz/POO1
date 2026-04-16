class Cereal:
    def __init__(self, marca, forma, sabor, color, tamaño):
        self.marca = marca
        self.forma = forma
        self.sabor = sabor
        self.color = color
        self.tamaño = tamaño

print(" ")
print("Primer Cereal")
print(" ")
#1 Cereal
mi_cereal1 = Cereal("Zucaritas", "redondas", "Dulce", "Amarillo", "Pequeño")
print(f"Marca: {mi_cereal1.marca}")
print(f"Forma: {mi_cereal1.forma}")
print(f"Sabor: {mi_cereal1.sabor}")
print(f"Color: {mi_cereal1.color}")
print(f"Tamaño: {mi_cereal1.tamaño}")

print(" ")
print("Siguiente Cereal")
print(" ")

#2 Cereal
mi_cereal2 = Cereal("Chocokrispis", "Ovalada", "Oreo", "Verde", "Grande")
print(f"Marca: {mi_cereal2.marca}")
print(f"Forma: {mi_cereal2.forma}")
print(f"Sabor: {mi_cereal2.sabor}")
print(f"Color: {mi_cereal2.color}")
print(f"Tamaño: {mi_cereal2.tamaño}") 
