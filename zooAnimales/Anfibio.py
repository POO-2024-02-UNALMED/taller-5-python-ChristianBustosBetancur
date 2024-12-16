from zooAnimales.Animal import Animal

class Anfibio(Animal):
    listado = []
    _ranas = 0
    _salamandras = 0

    def __init__(self, nombre="", edad=0, habitat="", genero="", color_piel="", venenoso=False):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = color_piel
        self._venenoso = venenoso
        Anfibio.listado.append(self)


    @staticmethod
    def cantidadAnfibios():
        return len(Anfibio.listado)

    @staticmethod
    def crearRana(nombre, edad, genero):
        Anfibio._ranas += 1
        Animal._totalAnimales += 1
        return Anfibio(nombre, edad, "selva", genero, "rojo", True)

    @staticmethod
    def crearSalamandra(nombre, edad, genero):
        Anfibio._salamandras += 1
        Animal._totalAnimales += 1
        return Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)

    def movimiento(self):
        return "saltar"

    def getColorPiel(self):
        return self._colorPiel

    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel

    def isVenenoso(self):
        return self._venenoso

    def setVenenoso(self, venenoso):
        self._venenoso = venenoso

    @staticmethod
    def getListado():
        return Anfibio.listado

    @staticmethod
    def setListado(listado):
        Anfibio.listado = listado
