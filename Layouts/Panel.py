# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from flet import Page, UserControl, Container, Column, Row, Text, ProgressRing, colors, Divider

class Panel(UserControl):
    def __init__(self, sayfa:Page):
        super().__init__()
        self.sayfa = sayfa

        self.baslik      = Text("NTV Son Dakika Haberleri", size=22, weight="bold", color="#EF7F1A")
        self.araniyor    = ProgressRing(visible=True)
        self.cikti_alani = Text("Son dakika haberleri aranıyor..", size=18, weight="bold", color=colors.CYAN_700, visible=True)

    def build(self):
        return Container(
            Column(
                width    = 500,
                controls = [
                    Row([self.baslik],      alignment="center"),
                    Divider(),
                    Row([self.araniyor],    alignment="center"),
                    Row([self.cikti_alani], alignment="center"),
                    Row(),
                    Divider()
                ]
            )
        )