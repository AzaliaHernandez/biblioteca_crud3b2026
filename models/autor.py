class Autor:
#constructor
    def __init__(self,id,nombre):
        self.id=id
        self.nombre = nombre

    def mostrar_info(self):
        return f"ID: {self.id}, NOMBRE: {self.nombre}"