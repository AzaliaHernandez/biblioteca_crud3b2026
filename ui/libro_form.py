import flet as ft

from models.libro import Libro
from dao.libro_dao import LibroDAO

def libro_form(regresar):
    titulo_input=ft.TextField(
        label="Titulo del libro",
        width=400
    )
    autor_input=ft.TextField(
        label="Autor del libro:",
        width=400
    )
    isbn_input=ft.TextField(
        label="ISBN del libro:",
        width=400
    )
    mensaje=ft.Text(
        "",
        color=ft.Colors.GREEN,
        size=16,
        weight=ft.FontWeight.BOLD
    )

    def guardar_libro(e):
        #recuperar los valores de los texfield
        titulo=titulo_input.value #variable =nombreTextfield.value
        autor=autor_input.value
        isbn=isbn_input.value

        #validar que los campos no esten vacios
        if titulo=="" or autor=="" or isbn=="":
            mensaje.value="Todos los campos son obligatorios"
            mensaje.color=ft.Colors.RED
            e.page.update()
            return
        
        try:

            libro_dao=LibroDAO()
            id=libro_dao.obtener_ultimo_id()+1
            nuevo_libro=Libro(
                id=id,
                titulo=titulo,
                autor=int(autor),
                isbn=isbn,
                disponible=True
            )
            libro_dao.insertar(nuevo_libro)


            mensaje.value=f"Libro '{titulo}' ha sido registrado con éxito"    
            mensaje.color=ft.Colors.GREEN
            
            #limpiar los textfield
            titulo_input.value=""
            autor_input.value=""
            isbn_input.value=""
            titulo_input.focus() 
        except  ValueError:
            #Manejo del error cuando el usario escribe texto en texfield del autor
            mensaje.value="El autor debe de ser un  numero entero"
            mensaje.color=ft.Colors.RED
        except Exception as error:
            mensaje.value=f"Error al registrar el libro: {error}"  
            mensaje.color=ft.Colors.RED 

        e.page.update()    


    return ft.Container(
        padding=30,
        content=ft.Column(
            controls=[
                ft.Text(
                    "Registro de nuevo libro",
                    size=24,
                    weight=ft.FontWeight.BOLD
                ),
                ft.Text(
                    "Capture los datos basicos del libro",
                    size=16,
                    color=ft.Colors.BLUE_GREY_600
                ),
                titulo_input,
                autor_input,
                isbn_input,

                ft.ElevatedButton(
                    "Guardar",
                    icon=ft.Icons.SAVE,
                    on_click=guardar_libro
                ),
                ft.OutlinedButton(
                    "Ir al inicio",
                    icon=ft.Icons.ARROW_BACK,
                    on_click=lambda e: regresar()
                ),
                mensaje
            ],
            spacing=15
        )
    )