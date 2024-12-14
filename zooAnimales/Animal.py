from zooAnimales import Anfibio, Ave, Mamifero, Pez, Reptil


class Animal:
    total_animales = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.zona = None
        Animal.total_animales += 1

    def movimiento(self):
        return "desplazarse"

    @staticmethod
    def total_por_tipo():
        return (f"Mamiferos: {Mamifero.cantidad_mamiferos()}\n"
                f"Aves: {Ave.cantidad_aves()}\n"
                f"Reptiles: {Reptil.cantidad_reptiles()}\n"
                f"Peces: {Pez.cantidad_peces()}\n"
                f"Anfibios: {Anfibio.cantidad_anfibios()}")

    def __str__(self):
        if self.zona:
            return (f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat} y mi genero es {self.genero}, "
                    f"la zona en la que me ubico es {self.zona.nombre}, en el {self.zona.zoo.nombre}")
        else:
            return (f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat} y mi genero es {self.genero}")