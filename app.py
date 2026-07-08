from dao.libro_dao import LibroDAO
from models.libro import Libro
from dao.usuario_dao import UsuarioDAO
from models.usuario import Usuario
def ver_libros():
    try:
            libro_dao=LibroDAO()
            libros =libro_dao.obtener_todo()
            if len(libros)==0:
                print("No hay libros registrados")
            else:
                for libro in libros:
                    print(f"{libro.id} - {libro.titulo} -{libro.autor}- {libro.isbn} -{libro.disponible}")
                print("\n Conexion exitosa con la base de datos")
    except Exception as e:
                print("ERROR")
                print(e)

def insertar_libro():
    print("INSERTAR UN NUEVO LIBRO")
    titulo=input("Escribe el titulo:")
    autor=int(input("Escribe el id del autor:"))
    isbn=input("escribe el isbn")
    disponible=True
    
    try:
        
        libro_dao=LibroDAO()
        ultimo_id=libro_dao.obtener_ultimo_id()+1
        libro=Libro(ultimo_id,titulo,autor,isbn,disponible)
        libro_dao.insertar(libro)
        print("La inserccion del nuevo libro fue exitosa")
    except Exception as e:
        print("Error al insertar el libro")    
        print(e)


def actualizar_libro ():
    try:
        libro_dao=LibroDAO()
        print("Lista de libros disponibles") 
        ver_libros()
        id=int(input("Selelciona el id del libro a actualizar: "))    
        titulo=input("Escribe el titulo del libro:")
        autor=int(input("Escribe el id del autor:"))
        isbn=input("Escribe el ISBN")
        disponible=bool(input("Escribe si el libro esta disponible:"))
        libro=Libro(id,titulo,autor,isbn,disponible)   
        libro_dao.actualizar(libro)
        print("El libro fue actualizado con exito:")
    except Exception as e:
        print("ERRROR al actualizar el libro")
        print(e)

def eliminar_libro ():
    try:
        libro_dao=LibroDAO()       
        print("Lista de libros disponibles: ")
        ver_libros()
        id=int(input("Escribe el id del libro que va eliminar:"))
        libro_dao.eliminar(id)
        print(f"El libro {id} ha sido eleminado con exito")
    except Exception as e: 
        print(f"Error al eliminar el libro{id}")     
        print(e)

def menu_libros  ():
    print("1.VER TODOS LOS LIBROS")
    print("2.INSERTAR UN NUEVO LIBBRO")
    print("3.ACTUALIZAR UN LIBRO EXISTENTE")
    print("4.ELIMINAR UN LIBRO EXISTENTE")
    opcion=int(input("Selecciona una opcion (1-4):"))

    match opcion:
        case 1:
            ver_libros()
        case 2:
            insertar_libro()
        case 3:
            actualizar_libro()
        case 4:
            eliminar_libro()        



def ver_usuarios():
    try:
            usuario_dao=UsuarioDAO()
            lista=usuario_dao.obtener_todo()
            if len(lista)==0:
                print("No hay usuarios registrados")
            else:
                for usuario in  lista:
                    print(f"{usuario.id} - {usuario.nombre} -{usuario.matricula}- {usuario.correo} -{usuario.activo}")
                print("\n Conexion exitosa con la base de datos")
    except Exception as e:
                print("ERROR")
                print(e)

def insertar_usuarios():
    print("INSERTAR UN NUEVO USUARIO")
    nombre=input("Escribe el Nombre:")
    carrera=int(input("Escribe la carrera: "))
    matricula=input("Escribe la matricula: ")
    correo=input("Escribe su correo: ")
    activo=True
    
    try:
        
        usuario_dao=UsuarioDAO()
        ultimo_id=usuario_dao.obtener_ultimo_id()+1
        usuarios=Usuario(ultimo_id,nombre,carrera,matricula,correo,activo)
        usuario_dao.insertar(usuarios)
        print("La inserccion del nuevo usuario fue exitosa")
    except Exception as e:
        print("Error al insertar el Usuario")    
        print(e)

def actualizar_usuarios ():
    try:
        usuario_dao=UsuarioDAO()
        print("Lista de usuarios ") 
        ver_usuarios()
        id=int(input("Selelciona el id del usuario a actualizar")) 
        # 1. Buscamos los datos vigentes del usuario
        usuario_actual=usuario_dao.obtener_por_id(id)
        
        if usuario_actual is None:
            print("El usuario no existe.")
            return

        print("1. Cambiar Carrera")
        print("2. Cambiar Matrícula")
        print("3. Cambiar Correo")
        print("4. Cambiar Estado (Activo/Inactivo)")
        print("5. Cambiar Todos los campos")
        opcion=input("¿Qué atributo deseas modificar?: ")

        
        if opcion == "1":
            usuario_actual.carrera=int(input(f"Nueva carrera: "))
        elif opcion == "2":
            usuario_actual.matricula=input(f"Nueva matrícula: ")
        elif opcion == "3":
            usuario_actual.correo=input(f"Nuevo correo : ")
        elif opcion == "4":
            estado=input(f"¿Está activo? true/false : ")
            usuario_actual.activo= True if estado.lower() == 'true' else False
        elif opcion == "5":
            usuario_actual.carrera=int(input("Escribe la nueva carrera:"))
            usuario_actual.matricula=input("Escribe la nueva matricula:")
            usuario_actual.correo=input("Escribe su correo :")
            estado=input("Escribe si esta activo (true o false):")
            usuario_actual.activo= True if estado.lower() == 'true' else False
        else:
            print("Opción no válida.")
            return
        
        usuario_dao.actualizar(usuario_actual)
        print("El usuario fue actualizado con exito")



    except Exception as e:
        print("ERRROR al actualizar el usuario")
        print(e)

def eliminar_usuarios ():
    try:
        usuario_dao=UsuarioDAO()       
        print("Lista de usuarios")
        ver_usuarios()
        id=int(input("Escribe el id del usuario que va eliminar:"))
        usuario_dao.eliminar(id)
        print(f"El usuario {id} ha sido eliminado con exito")
    except Exception as e: 
        print(f"Error al eliminar el usuario{id}")     
        print(e)



def menu_usuario  ():
    print("1.VER TODOS LOS USUARIOS")
    print("2.INSERTAR UN NUEVO USUARIO")
    print("3.ACTUALIZAR UN USUARIO EXISTENTE")
    print("4.ELIMINAR UN USUARIO EXISTENTE")
    opcion=int(input("Selecciona una opcion (1-4):"))

    match opcion:
        case 1:
            ver_usuarios()
        case 2:
            insertar_usuarios()
        case 3:
            actualizar_usuarios()
        case 4:
            eliminar_usuarios()      


def main():
    print("===BIBLIOTECA UNIVERSITARIA===")
    print("Menu de opciones:")
    print("1.Libros ")
    print("2.Usuarios")  
    opcion=int(input("Escribe tu opcion: "))
    match opcion:
        case 1:menu_libros()
        case 2:menu_usuario()
    print("Saliendo del sistema de la biblioteca universitaria ...")    



if __name__=="__main__":
    main()       
