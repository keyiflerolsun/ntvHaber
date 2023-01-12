# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from flet.page import Page, Event

class KekikFlet:
    def __init__(self, sayfa:Page, baslik:str):
        sayfa.title                = baslik
        sayfa.horizontal_alignment = "center"
        sayfa.vertical_alignment   = "center"
        sayfa.theme_mode           = "dark"
        sayfa.scroll               = "adaptive"
        # sayfa.auto_scroll          = True
        sayfa.window_max_width     = 600

        self.sayfa = sayfa

        def kapanirken(event:Event):
            if event.data == "close":
                self.sayfa.window_destroy()

        self.sayfa.window_prevent_close = True
        self.sayfa.on_window_event      = kapanirken
        self.sayfa.update()