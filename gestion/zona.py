class Zona:
    def __init__(self, nombre=None, zoo=None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = []

    def cantidadAnimales(self):
        return len(self._animales)

    def agregarAnimales(self, Animal):
        self.animales.append(Animal)