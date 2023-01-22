# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from .CLI      import cikis_yap, hata_yakala

from flet      import FLET_APP, WEB_BROWSER
from flet      import app as flet
from flet.page import Page

import pystray
from PIL   import Image
from .Libs import dosya_ver

from .Layouts import KekikFlet, Panel, Haberler
from os       import name as sistem
from .Libs    import zamanlayici

ZAMANLA = False

def ana_sayfa(sayfa:Page):
    KekikFlet(sayfa, "ntvHaber | @KekikAkademi")

    panel = Panel(sayfa)
    sayfa.add(panel)

    haberler = Haberler(sayfa, panel)
    sayfa.add(haberler)

    global ZAMANLA
    if not ZAMANLA:
        zamanlayici.add_job(haberler.haberleri_guncelle, args=[True], trigger="interval", minutes=1, id="haberleri_guncelle")
        ZAMANLA = True


    def __goster():
        sayfa.window_minimized = False
        sayfa.update()

    def __gizle():
        sayfa.window_minimized = True
        sayfa.update()

    simge_durum = pystray.Icon(
        name  = sayfa.title,
        icon  = Image.open(dosya_ver("Assets/Logo.png", 2)),
        title = sayfa.title,
        menu  = pystray.Menu(
            pystray.MenuItem("Göster", __goster),
            pystray.MenuItem("Gizle", __gizle),            
            pystray.MenuItem("Kapat", sayfa.window_destroy)
        )
    )
    simge_durum.run()


# if __name__ == "__main__":
def basla():
    try:
        zamanlayici.start()
        flet(target=ana_sayfa, view=FLET_APP if sistem != "nt" else WEB_BROWSER, port=1927, assets_dir="Assets")
        cikis_yap(False)
    except Exception as hata:
        hata_yakala(hata)