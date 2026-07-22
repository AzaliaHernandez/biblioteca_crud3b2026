import flet as ft
from ui.libro_form import libro_form
from ui.libros_list import libros_list

def main_window(page: ft.Page):

    #configurar pagina
    page.title="Sistema de gestion de biblioteca"
    page.window_width=1100
    page.window_heigth=700
    page.padding=0
    page.bgcolor=ft.Colors.BLUE_GREY_50

    #Elementos del contenedor principal
    titulo=ft.Text(
        "Sistema de Gestion de Biblioteca",
        size=24,
        weight=ft.FontWeight.BOLD
    )
    
    subtitulo=ft.Text(
        "Selecione una opcion del menu",
        size=16,
        color=ft.Colors.BLUE_GREY_600
    )

    #Creacion del contenedor
    contenido=ft.Container(
            padding=30,
            expand=True
        )
    def inicio():
            return ft.Column(
            controls=[
                titulo,
                subtitulo
            ] ,   
            spacing=10
        )
    
    def mostrar_inicio(e=None):
            contenido.content = inicio()
            page.update()

    #Menu lateral
    def mostrar_formulario_libro(e=None):
        contenido.content = libro_form(mostrar_inicio)
        page.update()

    def mostrar_lista_libros(e=None):
        contenido.content=libros_list(mostrar_inicio)  
        page.update()

    #crear el menu lateral 
    menu_lateral = ft.Container(
        width= 220,
        bgcolor= ft.Colors.BLUE_GREY_900,
            
        padding= 20,
        content= ft.Column(
            controls = [
                ft.Text(
                    "Biblioteca",
                    size = 22,
                    weight = ft.FontWeight.BOLD,
                    color = ft.Colors.WHITE
                ),
                ft.Text(
                    "Sistema de Gestion",
                    size = 12,
                    color = ft.Colors.WHITE
                ),
                ft.Divider(color = ft.Colors.BLUE_GREY_700),
                    #Botones
                ft.ElevatedButton(
                    "Inicio",
                    icon=ft.Icons.HOME,
                    width=180,
                    on_click=mostrar_inicio
                ),
                ft.ElevatedButton(
                    "Libros",
                    icon =ft.Icons.BOOK,
                    width = 180 ,
                    on_click= mostrar_lista_libros
                    ),
                    ft.ElevatedButton(
                    "Usuarios",
                    icon =ft.Icons.PERSON,
                    width = 180  
                    ),
                    ft.ElevatedButton(
                    "Prestamos",
                    icon =ft.Icons.SWAP_HORIZ,
                    width = 180  
                    ),
                    ft.ElevatedButton(
                    "Devoluciones",
                    icon =ft.Icons.KEYBOARD_RETURN,
                    width = 180  
                    ),
                ],
                spacing = 15
            )
        )
        
    #layout de la pagina
    layout=ft.Row(
        controls=[
            menu_lateral,
            contenido
        ],
        expand=True
    )
    
    page.add(layout)
    
    mostrar_inicio()

