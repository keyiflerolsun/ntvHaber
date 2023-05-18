# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from flet            import Page
from flet_core.event import Event

class KekikFlet:
    def __init__(self, sayfa:Page, baslik:str):
        sayfa.title                = baslik
        sayfa.horizontal_alignment = "center"
        sayfa.vertical_alignment   = "center"
        sayfa.theme_mode           = "dark"
        sayfa.scroll               = "adaptive"
        # sayfa.auto_scroll          = True

        sayfa.window_width     = 600
        sayfa.window_max_width = 600
        # sayfa.window_skip_task_bar = True

        self.sayfa = sayfa

        def kapanirken(event:Event):
            if event.data == "close":
                self.sayfa.window_destroy()

        self.sayfa.window_prevent_close = True
        self.sayfa.on_window_event      = kapanirken
        self.sayfa.update()