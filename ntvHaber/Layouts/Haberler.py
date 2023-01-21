# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from ..CLI     import konsol
from flet.page import Page
from flet      import UserControl, GridView, Container, Column, Text, colors, border, ImageFit 
from ..Libs    import sondakika_haberleri, bildirim

class Haberler(UserControl):
    def __init__(self, sayfa:Page, panel:Page):
        super().__init__()
        self.sayfa = sayfa

        self.haberler           = sondakika_haberleri()
        panel.araniyor.visible  = False
        panel.cikti_alani.value = f"{len(self.haberler)} adet son dakika haberi bulundu!"
        panel.cikti_alani.color = colors.GREEN_700
        panel.update()
        konsol.print(self.haberler)

        bildirim(
            baslik = "NTV Son Dakika Haberleri",
            icerik = f"{len(self.haberler)} adet son dakika haberi bulundu!"
        )

        self.resimler_satiri = GridView(expand=True, width=500, child_aspect_ratio=1.65)
        for haber in self.haberler:
            self.resimler_satiri.controls.append(self.__haber_ver(haber))

    def build(self):
        return Container(self.resimler_satiri)

    def __haber_ver(self, veri:dict) -> Container:
        return Container(
            expand        = True,
            border        = border.all(width=2, color="#EF7F1A"),
            border_radius = 12,
            padding       = 15,
            margin        = 5,
            content       = Column(
                horizontal_alignment = "center",
                alignment            = "center",
                controls             = [
                    Container(
                        expand        = 9,
                        border_radius = 12,
                        image_fit     = ImageFit.FILL,
                        image_src     = veri["gorsel"]
                    ),
                    Column(
                        alignment = "center",
                        expand    = 2,
                        controls  = [
                            Text(veri["haber"], size=18, weight="bold", text_align="center", color=colors.CYAN_700, no_wrap=False)
                        ]
                    )
                ]
            )
        )