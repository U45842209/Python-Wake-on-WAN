import re

import flet as ft


class ErrorTile(ft.Column):
    def __init__(self, error_name, error_delete):
        super().__init__()
        self.error_name = error_name
        self.error_delete = error_delete
        self.display_task = ft.Text(
            value=self.error_name
        )

        self.display_view = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ERROR_ROUNDED, color="#DC4C64"),
                            title=ft.Text("Erreur", color="#DC4C64", weight=ft.FontWeight.BOLD),
                            subtitle=self.display_task,
                            trailing=ft.IconButton(icon=ft.icons.DELETE_OUTLINE, on_click=self.delete_clicked,
                                                   tooltip="Supprimer")
                        ),
                    ]
                ),
                padding=0,
            ),
            color="#FFDCDC",
            col={"sm": 12, "md": 12, "lg": 12, "xl": 12},
        )

        self.controls = [self.display_view]

    def delete_clicked(self, e):
        self.error_delete(self)


class SuccessTile(ft.Column):
    def __init__(self, success_name, success_delete):
        super().__init__()
        self.success_name = success_name
        self.success_delete = success_delete
        self.display_task = ft.Text(
            value=self.success_name
        )

        self.display_view = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.CHECK_ROUNDED, color="#14A44D"),
                            title=ft.Text("Succès", color="#14A44D", weight=ft.FontWeight.BOLD),
                            subtitle=self.display_task,
                            trailing=ft.IconButton(icon=ft.icons.DELETE_OUTLINE, on_click=self.delete_clicked,
                                                   tooltip="Supprimer")
                        ),
                    ]
                ),
                padding=0,
            ),
            color="#DCFFDC",
            col={"sm": 12, "md": 12, "lg": 12, "xl": 12},
        )

        self.controls = [self.display_view]

    def delete_clicked(self, e):
        self.success_delete(self)


class assets_for_ui(ft.Container):

    def text_field(self):
        return ft.TextField(
            border_color="transparent",
            height=30,
            text_size=13,
            content_padding=0,
            cursor_color="black",
            cursor_width=1,
            cursor_height=18,
            color="black",
        )

    def text_field_container(self, name: str, control: ft.TextField, col):
        return ft.Container(
            height=55,
            bgcolor="#ebebeb",
            border_radius=6,
            padding=8,
            col=col,
            content=ft.Column(
                spacing=1,
                controls=[
                    ft.Text(value=name, size=9, color="black", weight=ft.FontWeight.BOLD),
                    control
                ],
            ),
        )

    def text_button(self, name: str, on_click: any):
        return ft.TextButton(
            text=name,
            height=60,
            on_hover=False,
            style=ft.ButtonStyle(overlay_color="#FF7900", color=ft.colors.BLACK,
                                 shape=ft.RoundedRectangleBorder(radius=6), animation_duration=500, bgcolor="#ebebeb"),
            on_click=on_click,
        )

    def text_button_container(self, control: ft.TextButton, col):
        return ft.Container(
            expand=True,
            height=55,
            border_radius=6,
            padding=0,
            bgcolor="transparent",
            content=control,
            col=col
        )
