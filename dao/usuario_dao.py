from database.conexion import Conexion
from models.usuario import Usuario

class UsuarioDAO:
    def obtener_todo(self):
        conexion=Conexion.obtener_conexion()
        cursor=conexion.cursor()

        

        cursor.execute("SELECT * FROM vista_usuarios")
        registros=cursor.fetchall()

        usuarios=[]
        for registro in registros:
            usuario =Usuario(
            id=registro[0],
            nombre= registro[1],
            carrera=registro[2],
            matricula=registro[3],
            correo=registro[4],
            activo=registro[5]
            )
            usuarios.append(usuario)
        cursor.close()
        conexion.close()
        return usuarios

    #insertar
    def insertar(self,usuario):
        conexion=Conexion.obtener_conexion()
        cursor=conexion.cursor()


        sql="""
        INSERT INTO usuario (id,nombre,carrera,matricula,correo,activo)
        VALUES ( %s, %s, %s , %s, %s,%s)
        """
            
        cursor.execute(sql,(
            usuario.id,
            usuario.nombre,
            usuario.carrera,
            usuario.matricula,
            usuario.correo,
            usuario.activo
            ))
        
        conexion.commit()
        cursor.close()
        conexion.close()

    #update   
    def actualizar(self,usuario):
        conexion=Conexion.obtener_conexion()
        cursor=conexion.cursor()

        sql="""
        UPDATE usuario
        SET nombre=%s,matricula=%s, carrera=%s, correo=%s, activo=%s
        WHERE id=%s
        """

        cursor.execute(sql,(
                       usuario.nombre,
                       usuario.carrera, 
                       usuario.matricula,
                       usuario.correo,
                       usuario.activo,
                       usuario.id
                       ))
        conexion.commit()
        cursor.close()
        conexion.close()


    def obtener_por_id(self, id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT id, nombre,matricula, carrera, correo, activo FROM usuario WHERE id=%s", (id,))
        registro = cursor.fetchone()

        cursor.close()
        conexion.close()
        
        if registro is None:
            return None
            
        
        # Mapeo corregido según el orden exacto de tu pgAdmin
        return Usuario(
            id=registro[0],       
            nombre=registro[1],    
            matricula=registro[2], 
            carrera=registro[3],  
            correo=registro[4],    
            activo=registro[5]     
        )
        

    def obtener_todo(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        # Forzamos el orden de las columnas en el SELECT para asegurar la consistencia
        cursor.execute("SELECT id, nombre, matricula, carrera, correo, activo FROM vista_usuarios")
        registros = cursor.fetchall()

        usuarios = []
        for registro in registros:
            usuario = Usuario(
                id=registro[0],
                nombre=registro[1],
                matricula=registro[2],
                carrera=registro[3],
                correo=registro[4],
                activo=registro[5]
            )
            usuarios.append(usuario)
            
        cursor.close()
        conexion.close()
        return usuarios
    #delete
    def eliminar(self,id) :

        conexion=Conexion.obtener_conexion()
        cursor=conexion.cursor()

        cursor.execute("DELETE FROM usuario WHERE id=%s",(id,))

        conexion.commit()
        cursor.close()
        conexion.close()

    def obtener_ultimo_id(self):
        conexion=Conexion.obtener_conexion()
        cursor=conexion.cursor()

        cursor.execute("SELECT MAX (id) FROM USUARIO")
        resultado=cursor.fetchone()

        cursor.close()
        conexion.close()
        
        if resultado[0] is None:
            return 0
        return resultado[0]
    
    
        