from zooAnimales import Animal

class Reptil(Animal):
    _listado = []
    _iguanas = 0
    _serpientes = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorEscamas=None, largoCola=None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil.listado.append(self)

    def movimiento(self):
        return "reptar"

    @staticmethod
    def getCantidadReptiles():
        return len(Reptil._listado)

    @staticmethod
    def crearIguana(nombre, edad, genero):
        Reptil._iguanas += 1
        Animal._totalAnimales += 1
        return Reptil(nombre, edad, "humedal", genero, "verde", 3)

    @staticmethod
    def crearSerpiente(nombre, edad, genero):
        Reptil._serpientes += 1
        Animal._totalAnimales += 1
        return Reptil(nombre, edad, "jungla", genero, "blanco", 1)
    
    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self, color_escamas):
        self._colorEscamas = color_escamas

    def getLargoCola(self):
        return self._largoCola

    def setLargoCola(self, largo_cola):
        self._largoCola = largo_cola