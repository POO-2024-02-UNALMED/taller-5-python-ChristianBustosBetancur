from zooAnimales import animal

class reptil(animal):
    listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, color_escamas=None, largo_cola=None):
        super().__init__(nombre, edad, habitat, genero)
        self.color_escamas = color_escamas
        self.largo_cola = largo_cola
        Reptil.listado.append(self)

    def movimiento(self):
        return "reptar"

    @staticmethod
    def cantidad_reptiles():
        return len(Reptil.listado)

    @staticmethod
    def crear_iguana(nombre, edad, genero):
        Reptil.iguanas += 1
        return Reptil(nombre, edad, "humedal", genero, "verde", 3)

    @staticmethod
    def crear_serpiente(nombre, edad, genero):
        Reptil.serpientes += 1
        return Reptil(nombre, edad, "jungla", genero, "blanco", 1)