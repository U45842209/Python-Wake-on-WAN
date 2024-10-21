import flet as ft


def setup(page):
    value = ft.AppBar(
        title=ft.Text("WakeOnWan", weight=ft.FontWeight.W_900, size=35, color="#111418"),
        center_title=False,
        bgcolor='#FF7900',
        actions=[
            ft.WindowDragArea(ft.IconButton(ft.icons.DRAG_INDICATOR, icon_color=ft.colors.BLACK)),
            ft.IconButton(ft.icons.CLOSE, on_click=lambda _: page.window_close(), icon_color=ft.colors.BLACK)
        ]
    )
    return value