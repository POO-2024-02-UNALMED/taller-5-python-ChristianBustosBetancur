from zooAnimales import Animal

class Ave(Animal):
    _listado = []
    _halcones = 0
    _aguilas = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorPlumas=None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)

    def movimiento(self):
        return "volar"

    @staticmethod
    def getCantidadAves():
        return len(Ave._listado)

    @staticmethod
    def crearHalcon(nombre, edad, genero):
        Ave._halcones += 1
        Animal._totalAnimales += 1
        return Ave(nombre, edad, "montanas", genero, "cafe glorioso")

    @staticmethod
    def crearAguila(nombre, edad, genero):
        Ave._aguilas += 1
        Animal._totalAnimales += 1
        return Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
    
    def getColorPlumas(self):
        return self._colorPlumas

    def setColorPlumas(self, color_plumas):
        self._colorPlumas = color_plumas