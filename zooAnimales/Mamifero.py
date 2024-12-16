from zooAnimales.Animal import Animal

class Mamifero(Animal):
    _listado = []
    _caballos = 0
    _leones = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, pelaje=None, patas=None):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)

    @staticmethod
    def getCantidadMamiferos():
        return len(Mamifero._listado)

    @staticmethod
    def crearCaballo(nombre, edad, genero):
        Mamifero._caballos += 1
        Animal._totalAnimales += 1
        return Mamifero(nombre, edad, "pradera", genero, True, 4)

    @staticmethod
    def crearLeon(nombre, edad, genero):
        Mamifero._leones += 1
        Animal._totalAnimales += 1
        return Mamifero(nombre, edad, "selva", genero, True, 4)
    
    def pelaje(self):
        return self._pelaje

    def setPelaje(self, pelaje):
        self._pelaje = pelaje

    def getPatas(self):
        return self._patas

    def setPatas(self, patas):
        self._patas = patas