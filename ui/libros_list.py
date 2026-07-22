import flet as ft
from dao.libro_dao import LibroDAO

def libros_list(regresar):
    tabla=ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Titulo")),
            ft.DataColumn(ft.Text("Autor")),
            ft.DataColumn(ft.Text("ISBN")),
            ft.DataColumn(ft.Text("Disponible"))
        ],
        rows=[]
    )

    mensaje=ft.Text()

    def cargar_libros():
        try:
            libro_dao=LibroDAO()
            libros=libro_dao.obtener_todo()

            tabla.rows.clear()

            for libro in libros:
                tabla.rows.append(
                    ft.DataRow(
                        cells=[

                            ft.DataCell(ft.Text(str(libro.id))),
                            ft.DataCell(ft.Text(libro.titulo)),
                            ft.DataCell(ft.Text(str(libro.autor))),
                            ft.DataCell(ft.Text(libro.isbn)),
                            ft.DataCell(ft.Text(str(libro.disponible)))

                            
                        ]  
                    )
                )
        except Exception as error:
            mensaje.value=f"error al consultar libros: {error}"     
            mensaje.color=ft.Colors.RED   
    cargar_libros()


    return ft.Container(
        padding=30,
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Column(
                            controls=(
                                ft.Text(
                                    "Libros registrados",
                                    size=24,
                                    weight=ft.FontWeight.BOLD
                                ),
                                ft.Text(
                                    "Consulta de libros disponibles",
                                    color=ft.Colors.BLUE_GREY_600
                                )
                            )
                        ),
                        ft.OutlinedButton(
                            "Regresar",
                            icon=ft.Icons.ARROW_BACK,
                            on_click=regresar
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Divider(),

                ft.Container(
                    content=tabla,
                    border=ft.Border.all(
                        1,
                        ft.Colors.BLUE_GREY_200

                    ),
                    border_radius=10,
                    padding=10
                ),
                mensaje
            ],
            spacing=20,
            scroll=ft.ScrollMode.AUTO
        )
    )        