# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from ..Libs.NTV import sondakika_haberleri
from notifypy   import Notify
import os

ust_dizin_ver = lambda _path, n: os.sep.join(_path.split(os.sep)[:-n])

def dosya_ver(dosya_yolu:str, ust_dizin:int):
    return os.path.join(ust_dizin_ver(__file__, ust_dizin), dosya_yolu)

def bildirim(baslik:str, icerik:str):

    _bildirim = Notify()
    _bildirim._notification_application_name = "ntvHaber | @KekikAkademi"
    _bildirim._notification_icon             = dosya_ver("Assets/Logo.png", 2)

    if os.name == "nt":
        _bildirim.icon = dosya_ver("Assets/Logo.png", 2)

    _bildirim.title   = baslik
    _bildirim.message = icerik

    _bildirim.send(block=False)

from apscheduler.schedulers.background import BackgroundScheduler

zamanlayici = BackgroundScheduler(timezone="Europe/Istanbul", job_defaults={"misfire_grace_time": 15*60})