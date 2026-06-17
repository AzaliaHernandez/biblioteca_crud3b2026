from models.libro import Libro
class Prestamo:
    
    def __init__(self,id, libro, usuario, fecha_prestamo, fecha_devolucion,estado):
        self.id = id 
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.estado =  estado

    def registrar_devolucion(self, fecha_devolucion):
        self.fecha_devolucion = fecha_devolucion
        self.estado = "Devuelto "
        self.libro.devolver()