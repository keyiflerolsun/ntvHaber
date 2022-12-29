# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from ..CLI     import konsol

from flet.page import Page
from flet      import (
    UserControl,
    colors,
    Container,
    padding,
    border,
    border_radius,
    Column,
    Row,
    Image,
    ImageFit,
    ImageRepeat,
    Text,
    TextAlign,
    Divider
)

from ..Libs import sondakika_haberleri, bildirim

class Haberler(UserControl):
    def __init__(self, sayfa:Page, panel:Page):
        super().__init__()
        self.sayfa = sayfa

        self.haberler = sondakika_haberleri()
        panel.araniyor.visible  = False
        panel.cikti_alani.value = f"{len(self.haberler)} adet haber bulundu."
        panel.cikti_alani.color = colors.GREEN_700
        panel.update()
        konsol.print(self.haberler)

        bildirim(
            baslik = "NTV Son Dakika Haberleri",
            icerik = f"{len(self.haberler)} adet haber bulundu."
        )

        self.resimler_satiri = Column(alignment="center", width=350)
        for haber in self.haberler:
            self.resimler_satiri.controls.append(self.__haber_ver(haber))
            self.resimler_satiri.controls.append(Column([Divider()]))
        self.resimler_satiri.controls.pop(-1)

    def build(self):
        return Container(self.resimler_satiri)

    def __haber_ver(self, veri:dict) -> Container:
        return Container(
            Column(
                [
                    Row(
                        [
                            Image(
                                src           = veri["gorsel"],
                                width         = 200,
                                height        = 200,
                                fit           = ImageFit.NONE,
                                repeat        = ImageRepeat.NO_REPEAT,
                                border_radius = border_radius.all(10)
                            )
                        ],
                        alignment="center"
                    ),
                    Row([Text(veri["haber"], size=18, width=300, weight="bold", text_align=TextAlign.CENTER, color=colors.CYAN_700)], alignment="center")
                ]
            ),
            width         = 350,
            padding       = padding.all(10),
            border_radius = border_radius.all(10),
            border        = border.all(width=2, color="#EF7F1A")
        )