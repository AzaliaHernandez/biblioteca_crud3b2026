import flet as ft

def libro_form():
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
                    icon=ft.Icons.SAVE
                ),
                mensaje
            ],
            spacing=15
        )
    )