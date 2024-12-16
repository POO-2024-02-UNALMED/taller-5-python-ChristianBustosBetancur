
from zooAnimales import Anfibio, Ave, Mamifero, Pez, Reptil


class Animal:
    _totalAnimales = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        Animal._totalAnimales += 1

    def movimiento(self):
        return "desplazarse"

    @staticmethod
    def totalPorTipo():
        return (f"Mamiferos: {Mamifero._getCantidadMamiferos()}\n"
                f"Aves: {Ave._getCantidadAves()}\n"
                f"Reptiles: {Reptil._getCantidadReptiles()}\n"
                f"Peces: {Pez._getCantidadPeces()}\n"
                f"Anfibios: {Anfibio._getCantidadAnfibios()}")

    def __str__(self):
        if self.zona:
            return (f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, "
                    f"la zona en la que me ubico es {self.zona._nombre}, en el {self.zona.zoo._nombre}")
        else:
            return (f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self._habitat} y mi genero es {self._genero}")

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad

    def setEdad(self, edad):
        self._edad = edad

    def getHabitat(self):
        return self._habitat

    def setHabitat(self, habitat):
        self._habitat = habitat

    def getGenero(self):
        return self._genero

    def setGenero(self, genero):
        self._genero = genero

    def getZona(self):
        return self._zona

    def setZona(self, zona):
        self._zona = zona