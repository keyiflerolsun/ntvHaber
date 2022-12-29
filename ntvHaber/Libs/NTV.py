# Bu Araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from requests import get

def sondakika_haberleri():
    istek = get("https://kolektifapi.kekikakademi.org/haber")
    return istek.json()["veri"]