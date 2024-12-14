class Zona:
    def __init__(self, nombre=None, zoo=None):
        self.nombre = nombre
        self.zoo = zoo
        self.animales = []

    def cantidad_animales(self):
        return len(self.animales)

    def agregar_animales(self, animal):
        self.animales.append(animal)