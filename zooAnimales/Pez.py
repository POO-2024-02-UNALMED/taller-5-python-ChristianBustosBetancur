from zooAnimales import Animal

class Pez(Animal):
    _listado = []
    _salmones = 0
    _bacalaos = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorEscamas=None, cantidadAletas=None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez._listado.append(self)

    def movimiento(self):
        return "nadar"

    @staticmethod
    def getCantidadPeces():
        return len(Pez._listado)

    @staticmethod
    def crearSalmon(nombre, edad, genero):
        Pez._salmones += 1
        Animal._totalAnimales += 1
        return Pez(nombre, edad, "oceano", genero, "rojo", 6)

    @staticmethod
    def crearBacalao(nombre, edad, genero):
        Pez._bacalaos += 1
        Animal._totalAnimales += 1
        return Pez(nombre, edad, "oceano", genero, "gris", 6)
    
    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self, color_escamas):
        self._colorEscamas = color_escamas

    def getCantidadAletas(self):
        return self._cantidadAletas

    def setCantidadAletas(self, cantidad_aletas):
        self._cantidadAletas = cantidad_aletas