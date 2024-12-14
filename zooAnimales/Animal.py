from zooAnimales import Anfibio, Ave, Mamifero, Pez, Reptil


class Animal:
    _totalAnimales = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        Animal.totalAnimales += 1

    def movimiento(self):
        return "desplazarse"

    @staticmethod
    def total_por_tipo():
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