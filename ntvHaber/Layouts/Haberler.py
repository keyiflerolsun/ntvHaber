# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from ..CLI     import konsol
from flet.page import Page
from flet      import UserControl, GridView, Container, Column, Text, colors, border, ImageFit 
from ..Libs    import sondakika_haberleri, bildirim

class Haberler(UserControl):
    def __init__(self, sayfa:Page, panel:Page):
        super().__init__()
        self.sayfa = sayfa

        self.panel    = panel
        self.haberler = []
        self.__paneli_guncelle()

        self.haberler_grid = GridView(expand=True, width=550, child_aspect_ratio=1.3)
        self.haberleri_guncelle()


    def build(self):
        return Container(self.haberler_grid)

    def __haber_konteyner(self, veri:dict) -> Container:
        return Container(
            border        = border.all(width=2, color="#EF7F1A"),
            border_radius = 12,
            padding       = 15,
            margin        = 5,
            content       = Column(
                horizontal_alignment = "center",
                alignment            = "center",
                controls             = [
                    Text(veri["haber"], size=18, weight="bold", text_align="center", color=colors.CYAN_700, no_wrap=False),
                    Container(
                        expand        = True,
                        border_radius = 12,
                        image_fit     = ImageFit.FILL,
                        image_src     = veri["gorsel"]
                    ),
                    Text(veri["detay"], size=16, no_wrap=False)
                ]
            )
        )

    def haberleri_guncelle(self, guncelle:bool=False):
        if guncelle:
            self.__paneli_guncelle()

        if self.haberler:
            self.__sayfayi_guncelle()

    def __paneli_guncelle(self):
        self.panel.cikti_alani.color = colors.CYAN_700
        self.panel.cikti_alani.value = "Son dakika haberleri güncelleniyor.."
        self.panel.araniyor.visible  = True
        self.panel.update()
        self.sayfa.update()

        self.haberler = sondakika_haberleri()

        self.panel.araniyor.visible  = False
        self.panel.cikti_alani.color = colors.GREEN_700
        self.panel.cikti_alani.value = "Son dakika haberleri güncellendi!"
        self.panel.update()
        self.sayfa.update()

    def __sayfayi_guncelle(self):
        if self.haberler_grid.controls:
            self.haberler_grid.controls.clear()

        if len(self.haberler) > 20:
            bildirim(
                baslik = "NTV Son Dakika Haberleri",
                icerik = f"{len(self.haberler)} adet son dakika haberi bulundu!"
            )


        for haber in self.haberler:
            self.haberler_grid.controls.append(self.__haber_konteyner(haber))
            konsol.log(haber)

            if len(self.haberler) < 20:
                bildirim(
                    baslik = haber["haber"],
                    icerik = haber["detay"]
                )

        self.sayfa.update()