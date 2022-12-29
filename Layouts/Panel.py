# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from flet.page import Page
from flet      import UserControl, Container, Column, Row, Text, ProgressRing, colors

class Panel(UserControl):
    def __init__(self, sayfa:Page):
        super().__init__()
        self.sayfa = sayfa

        def kapanirken(e):
            if e.data == "close":
                self.sayfa.window_destroy()

        self.sayfa.window_prevent_close = True
        self.sayfa.on_window_event      = kapanirken
        self.sayfa.update()

        self.baslik      = Text("NTV Son Dakika Haberleri", size=22, weight="bold", color="#EF7F1A")
        self.araniyor    = ProgressRing(visible=True)
        self.cikti_alani = Text("Son dakika haberleri aranıyor..", size=18, weight="bold", color=colors.CYAN_700, visible=True)

    def build(self):
        return Container(
            Column(
                [
                    Row([self.baslik],      alignment="center"),
                    Row([self.araniyor],    alignment="center"),
                    Row([self.cikti_alani], alignment="center")
                ]
            )
        )