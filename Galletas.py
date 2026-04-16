class Galletas:
    def __init__(self, sabor, forma, color, marca, desea_glaseado, glaseado):
        self.sabor = sabor
        self.forma = forma
        self.color = color
        self.marca = marca
        self.desea_glaseado = desea_glaseado
        self.glaseado = glaseado

print(" ")
print("Primer Galleta")
print(" ")

#1 Galleta
mi_galleta1 = Galletas("Vainilla", "Cuadrada", "Verde","Si", "Festival", "Coco")
print(f"Sabor: {mi_galleta1.sabor}")
print(f"Forma: {mi_galleta1.forma}")
print(f"Color: {mi_galleta1.color}")
print(f"Marca: {mi_galleta1.marca}")
print(f"Desea Glaseado:  {mi_galleta1.desea_glaseado}")
print(f"Glaseado: {mi_galleta1.glaseado}")

print(" ")
print("Siguiente Galleta")
print(" ")

#2 Galleta
mi_galleta2 = Galletas("Chocolate", "Estrella", "Vinotinto", "Caravana","No", "Nulo")
print(f"Sabor: {mi_galleta2.sabor}")
print(f"Forma: {mi_galleta2.forma}")
print(f"Color: {mi_galleta2.color}")
print(f"Marca: {mi_galleta2.marca}")
print(f"Desea Glaseado:  {mi_galleta2.desea_glaseado}")
print(f"Glaseado: {mi_galleta2.glaseado}")

print(" ")
print("Siguiente Galleta")
print(" ")

#3 Galleta
mi_galleta3 = Galletas("Milo", "Redondas", "Cafe", "Nestle","Si", "Milo")
print(f"Sabor: {mi_galleta3.sabor}")
print(f"Forma: {mi_galleta3.forma}")
print(f"Color: {mi_galleta3.color}")
print(f"Marca: {mi_galleta3.marca}")
print(f"Desea Glaseado:  {mi_galleta3.desea_glaseado}")
print(f"Glaseado: {mi_galleta3.glaseado}")

