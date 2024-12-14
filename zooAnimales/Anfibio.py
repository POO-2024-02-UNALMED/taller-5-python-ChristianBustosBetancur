from zooAnimales import Animal

class Anfibio(Animal):
    _listado = []
    _ranas = 0
    _salamandras = 0

    def __init__(self, nombre="", edad=0, habitat="", genero="", color_piel="", venenoso=False):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = color_piel
        self._venenoso = venenoso
        Anfibio.listado.append(self)

    @staticmethod
    def cantidad_anfibios():
        return len(Anfibio._listado)

    @staticmethod
    def crear_rana(nombre, edad, genero):
        rana = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        Anfibio.ranas += 1
        return rana

    @staticmethod
    def crear_salamandra(nombre, edad, genero):
        salamandra = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        Anfibio._salamandras += 1
        return salamandra

    def movimiento(self):
        return "saltar"

    # Getters and Setters
    def getColorPiel(self):
        return self._colorPiiel

    def setcolorPiel(self, colorPiel):
        self._colorPiel = colorPiel

    def isVenenoso(self):
        return self._venenoso

    def set_venenoso(self, venenoso):
        self._venenoso = venenoso

    @staticmethod
    def getListado():
        return Anfibio._listado

    @staticmethod
    def setListado(listado):
        Anfibio._listado = listado