class Zoologico:
    def __init__(self, nombre=None, ubicacion=None):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []

    def agregarzonas(self, zona):
        self._zonas.append(zona)

    def cantidadAnimales(self):
        return sum(zona.cantidadAnimales() for zona in self.zonas)