from zooAnimales import animal

class ave(animal):
    listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, color_plumas=None):
        super().__init__(nombre, edad, habitat, genero)
        self.color_plumas = color_plumas
        Ave.listado.append(self)

    def movimiento(self):
        return "volar"

    @staticmethod
    def cantidad_aves():
        return len(Ave.listado)

    @staticmethod
    def crear_halcon(nombre, edad, genero):
        Ave.halcones += 1
        return Ave(nombre, edad, "montanas", genero, "cafe glorioso")

    @staticmethod
    def crear_aguila(nombre, edad, genero):
        Ave.aguilas += 1
        return Ave(nombre, edad, "montanas", genero, "blanco y amarillo")