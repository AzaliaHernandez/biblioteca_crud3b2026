class Usuario:

    def __init__(self, id, nombre,  carrera, matricula, correo, activo):
        self.id = id 
        self.nombre = nombre
        self.carrera = carrera
        self.matricula = matricula
        
        self.correo = correo
        self.activo = activo

    def activar(self):
        self.activo = False

    def desactivar(self):
        self.activo = False

    def mostrar_info(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Matricula: {self.matricula}, Carrera: {self.carrera}, Activo: {self.activo}"            