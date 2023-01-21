# Bu Araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from ..CLI    import konsol
from requests import get
from parsel   import Selector

RAMBASE = []

def detay_ver(veriler:list) -> list:
    haberler = []
    for haber in veriler:
        istek  = get(haber["link"])
        secici = Selector(istek.text)

        haber["detay"] = secici.xpath("normalize-space(//h2[@class='category-detail-sub-title'])").get().replace("SON DAKİKA HABERİ:", "").replace(" | Son depremler", "").replace("SON DAKİKA: ", "").replace("SON DAKİKA:", "").strip()
        haberler.append(haber)

    return haberler

def sondakika_haberleri() -> list:
    konsol.log("[yellow]sondakika_haberleri() fonksiyonu çalıştırıldı...[/]")

    global RAMBASE

    istek    = get("https://kolektifapi.kekikakademi.org/haber")
    haberler = istek.json()["veri"]

    detay_sor = []
    for haber in haberler:
        if haber["haber"] in RAMBASE:
            continue

        RAMBASE.append(haber["haber"])
        detay_sor.append(haber)

    if not detay_sor:
        return []

    return detay_ver(detay_sor)