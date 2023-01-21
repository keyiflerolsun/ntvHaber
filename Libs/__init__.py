# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Libs.NTV import sondakika_haberleri
from notifypy import Notify
from os       import name as sistem
from pathlib  import Path

def bildirim(baslik:str, icerik:str):

    # calisma_dizini = Path(__file__).parent.resolve()

    # calisma_dizini = Path(__file__).parents[1]
    # ayrac          = "/" if sistem != "nt" else "\\"
    # logo_yolu      = f"{calisma_dizini}{ayrac}Assets{ayrac}Logo.png"

    _bildirim = Notify()
    _bildirim._notification_application_name = "ntvHaber | @KekikAkademi"
    _bildirim._notification_icon             = "Assets/Logo.png"

    if sistem == "nt":
        _bildirim.icon = "Assets/Logo.png"

    _bildirim.title   = baslik
    _bildirim.message = icerik

    _bildirim.send(block=False)

from apscheduler.schedulers.background import BackgroundScheduler

zamanlayici = BackgroundScheduler(timezone="Europe/Istanbul", job_defaults={"misfire_grace_time": 15*60})