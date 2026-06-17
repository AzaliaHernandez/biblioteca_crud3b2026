from database.conexion import Conexion
from models.libro import libro 

class LibroDAO:
    def obtener_todo(self):
        conexion=Conexion.obtener_conexion()
        cursor=conexion.cursor()

        cursor.excute("SELECT *FROM libro ")
        registros=cursor.fetchall()

        libros=[]
        for registro in registros:
            libro =libro(
            id=registro[0],
            autor=registro[1],
            isbn=registro[2],
            disponible=registro[3]
            )
            libros.append(libro)
        cursor.close()
        conexion.close()
        return libros

    def insertar(self,libro):
        conexion=Conexion.obtener_conexion()
        cursor=conexion.cursor()


        sql="""
        INSERT INTO libro(titulo,autor,isbn,disponible)
        VALUES ( %s, %s, %s , %s)
        """
            
        cursor.excute(sql,(
            libro.titulo,
            libro.autor,
            libro.isbn,
            libro.disponible
            ))
        
        conexion.commit()
        cursor.close()
        conexion.close()