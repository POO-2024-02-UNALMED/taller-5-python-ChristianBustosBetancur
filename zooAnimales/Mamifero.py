from zooAnimales.Animal import Animal

class Mamifero(Animal):
    listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, pelaje=None, patas=None):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero.listado.append(self)

    def __str__(self):
        return f"Mi nombre es {self._nombre}, tengo una edad de 
                {self._edad}, habito en {self._habitat}, mi género es 
                {self._genero}, {'tengo' if self._pelaje else 'no tengo'} 
                    pelaje y tengo {self._patas} patas"



    @staticmethod
    def getCantidadMamiferos():
        return len(Mamifero.listado)

    @staticmethod
    def crearCaballo(nombre, edad, genero):
        Mamifero.caballos += 1
        Animal._totalAnimales += 1
        return Mamifero(nombre, edad, "pradera", genero, True, 4)

    @staticmethod
    def crearLeon(nombre, edad, genero):
        Mamifero.leones += 1
        Animal._totalAnimales += 1
        return Mamifero(nombre, edad, "selva", genero, True, 4)
    
    @staticmethod
    def getCaballos():
        return Mamifero.caballos

    @staticmethod
    def getLeones():
        return Mamifero.leones
    
    def isPelaje(self):
        return self._pelaje

    def setPelaje(self, pelaje):
        self._pelaje = pelaje

    def getPatas(self):
        return self._patas

    def setPatas(self, patas):
        self._patas = patas