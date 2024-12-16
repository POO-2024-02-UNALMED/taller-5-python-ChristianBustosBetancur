from zooAnimales.Animal import Animal

class Reptil(Animal):
    listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorEscamas=None, largoCola=None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil.listado.append(self)
  
    def __str__(self):
        return f"Mi nombre es {self._nombre}, tengo una edad de 
        {self._edad}, habito en {self._habitat}, mi género es 
        {self._genero}, mi color de escamas es {self._colorEscamas}
        y mi largo de cola es {self._largoCola}"


    def movimiento(self):
        return "reptar"

    @staticmethod
    def getCantidadReptiles():
        return len(Reptil.listado)

    @staticmethod
    def crearIguana(nombre, edad, genero):
        Reptil.iguanas += 1
        Animal._totalAnimales += 1
        return Reptil(nombre, edad, "humedal", genero, "verde", 3)

    @staticmethod
    def crearSerpiente(nombre, edad, genero):
        Reptil.serpientes += 1
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
    
    @staticmethod
    def getListado():
        return Reptil._listado