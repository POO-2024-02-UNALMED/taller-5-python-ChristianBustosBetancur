from zooAnimales import Animal

class anfibio(Animal):
    listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre="", edad=0, habitat="", genero="", color_piel="", venenoso=False):
        super().__init__(nombre, edad, habitat, genero)
        self.color_piel = color_piel
        self.venenoso = venenoso
        Anfibio.listado.append(self)

    @staticmethod
    def cantidad_anfibios():
        return len(Anfibio.listado)

    @staticmethod
    def crear_rana(nombre, edad, genero):
        rana = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        Anfibio.ranas += 1
        return rana

    @staticmethod
    def crear_salamandra(nombre, edad, genero):
        salamandra = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        Anfibio.salamandras += 1
        return salamandra

    def movimiento(self):
        return "saltar"

    # Getters and Setters
    def get_color_piel(self):
        return self.color_piel

    def set_color_piel(self, color_piel):
        self.color_piel = color_piel

    def is_venenoso(self):
        return self.venenoso

    def set_venenoso(self, venenoso):
        self.venenoso = venenoso

    @staticmethod
    def get_listado():
        return Anfibio.listado

    @staticmethod
    def set_listado(listado):
        Anfibio.listado = listado