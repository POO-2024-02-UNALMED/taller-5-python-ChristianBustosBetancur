class Zoologico:
    def __init__(self, nombre=None, ubicacion=None):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.zonas = []

    def agregar_zonas(self, zona):
        self.zonas.append(zona)

    def cantidad_total_animales(self):
        return sum(zona.cantidad_animales() for zona in self.zonas)