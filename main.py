import flet as ft
from modules import appbar, waker, misc


class APP:

    def __init__(self, page: ft.Page, waker):
        super().__init__()

        self.ui = misc.assets_for_ui()

        self.page = page
        self.wak = waker

        self.main_column = ft.Column

        self.mac = self.ui.text_field()
        self.ip = self.ui.text_field()
        self.port = self.ui.text_field()

        self.submit = self.ui.text_button("Send", on_click=lambda e: self.action())

    def build(self):
        screen = ft.Container(
            self.main_column(
                [
                    ft.ResponsiveRow(
                        controls=[
                            self.ui.text_field_container("MAC address :", self.mac, col={"sm": 12, "md": 6, "lg": 5, "xl": 5}),
                            self.ui.text_field_container("IP address or FQDN :", self.ip,col={"sm": 12, "md": 6, "lg": 5, "xl": 5}),
                            self.ui.text_field_container("Port to be use (usually 7 or 9) :", self.port, col={"sm": 12, "md": 12, "lg": 2, "xl": 2}),
                        ]
                    ),
                    ft.ResponsiveRow(
                        [
                            self.ui.text_button_container(self.submit, col={"sm": 12, "md": 12, "lg": 12, "xl": 12})
                        ]
                    )
                ],
                col={"sm": 12, "md": 12, "lg": 12, "xl": 12}
            )
        )
        return screen

    def action(self):
        self.wak.makeMagicPacket(self.mac.value)
        self.wak.sendPacket(self.ip.value, int(self.port.value))




def main(page: ft.Page):
    app = APP(page, waker.Waker())
    page.appbar = appbar.setup(page)
    page.add(app.build())
    page.padding = 10
    #page.window.resizable = False
    page.window.min_height = 400
    page.window.height = 550
    page.window.min_width = 450
    page.window.width = 450
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.title_bar_hidden = True
    page.window.title_bar_buttons_hidden = True
    page.theme_mode = ft.ThemeMode.DARK

    page.update()


ft.app(target=main)