# 📰 ntvHaber

![Repo Boyutu](https://img.shields.io/github/repo-size/keyiflerolsun/ntvHaber?logo=git&logoColor=white)
![Görüntülenme](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://github.com/keyiflerolsun/ntvHaber&title=Görüntülenme)
<a href="https://KekikAkademi.org/Kahve" target="_blank"><img src="https://img.shields.io/badge/☕️-Kahve Ismarla-ffdd00" title="☕️ Kahve Ismarla" style="padding-left:5px;"></a>

![Python Version](https://img.shields.io/pypi/pyversions/ntvHaber?logo=python&logoColor=white)
![License](https://img.shields.io/pypi/l/ntvHaber?logo=gnu&logoColor=white)
![Status](https://img.shields.io/pypi/status/ntvHaber?logo=windowsterminal&logoColor=white)

[![PyPI](https://img.shields.io/pypi/v/ntvHaber?logo=pypi&logoColor=white)](https://pypi.org/project/ntvHaber)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/ntvHaber?logo=pypi&logoColor=white)](https://pypi.org/project/ntvHaber)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/ntvHaber?logo=pypi&logoColor=white)](https://pypi.org/project/ntvHaber)

[![PyPI Yükle](https://github.com/keyiflerolsun/ntvHaber/actions/workflows/pypiYukle.yml/badge.svg)](https://github.com/keyiflerolsun/ntvHaber/actions/workflows/pypiYukle.yml)

[![FlatHub](https://img.shields.io/flathub/v/org.kekikakademi.ntvHaber?logo=flathub&logoColor=white)](https://flathub.org/tr/apps/org.kekikakademi.ntvHaber)
[![FlatHub - Downloads](https://img.shields.io/flathub/downloads/org.kekikakademi.ntvHaber?logo=flathub&logoColor=white)](https://flathub.org/tr/apps/org.kekikakademi.ntvHaber)

**Python Yazılımların Python ve Flatpak olarak Paketlenme Örneği**

_[@flet-dev](https://github.com/flet-dev) ile.._

![ntvHaber](https://raw.githubusercontent.com/keyiflerolsun/ntvHaber/main/.github/icons/SS.png)

[![ForTheBadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-love](https://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/keyiflerolsun/)

## 🚀 Kurulum

### <img width="16" src="https://raw.githubusercontent.com/keyiflerolsun/ntvHaber/main/.github/icons/pypi.svg"> PyPi

```bash
# Yüklemek
pip install ntvHaber

# Güncellemek
pip install -U ntvHaber
```

### <img width="16" src="https://raw.githubusercontent.com/keyiflerolsun/ntvHaber/main/.github/icons/flathub.svg"> FlatHub

```bash
# Yüklemek
flatpak install flathub org.kekikakademi.ntvHaber

# Çalıştırmak
flatpak run org.kekikakademi.ntvHaber
```

## 📝 Kullanım

### <img width="16" src="https://raw.githubusercontent.com/keyiflerolsun/ntvHaber/main/.github/icons/freedesktop.svg"> UI

```bash
ntvHaber

# veya

flatpak run org.kekikakademi.ntvHaber
```

---

<details>
    <summary style="font-weight: bold; font-size: 20px">
      <img width="16" src="https://raw.githubusercontent.com/keyiflerolsun/ntvHaber/main/.github/icons/buddy.svg"> <b>Manuel Derlemek</b>
      <i>(genişletmek için tıklayın!)</i>
    </summary>
    <br/>

### <img width="16" src="https://raw.githubusercontent.com/keyiflerolsun/ntvHaber/main/.github/icons/python.svg"> Python

```bash
# Depoyu Çek
https://github.com/keyiflerolsun/ntvHaber.git
cd ntvHaber

# Gerekli Ortamları Kur
pip install -U pip setuptools wheel twine

# Paketi Yükle
pip install .

# Artıkları Temizle
rm -rf build *.egg-info

# Çalıştır
ntvHaber

# Paketi Kaldır
pip uninstall ntvHaber
```

### <img width="16" src="https://raw.githubusercontent.com/keyiflerolsun/ntvHaber/main/.github/icons/flatpak.svg"> FlatPak

```bash
# Depoyu Çek
git clone https://github.com/keyiflerolsun/ntvHaber.git
cd ntvHaber

# Dosyaları al
mv Shared/*.yml . && mv Shared/SRC .

# Gerekli Ortamları Kur
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
flatpak remote-add --if-not-exists flathub-beta https://flathub.org/beta-repo/flathub-beta.flatpakrepo
flatpak update && flatpak upgrade
flatpak install flathub org.freedesktop.{Platform,Sdk}//22.08

# Paketle
flatpak-builder --user --install --force-clean build-dir org.kekikakademi.ntvHaber.yml

# Artıkları Temizle
rm -rf .flatpak* .vscode build-dir && find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

# Çalıştır
flatpak run org.kekikakademi.ntvHaber

# Paketi Kaldır
flatpak uninstall org.kekikakademi.ntvHaber
```

</details>

---

## 🌐 Telif Hakkı ve Lisans

* *Copyright (C) 2023 by* [keyiflerolsun](https://github.com/keyiflerolsun) ❤️️
* [GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007](https://github.com/keyiflerolsun/ntvHaber/blob/master/LICENSE) *Koşullarına göre lisanslanmıştır..*

## ♻️ İletişim

*Benimle iletişime geçmek isterseniz, **Telegram**'dan mesaj göndermekten çekinmeyin;* [@keyiflerolsun](https://t.me/KekikKahve)

## 💸 Bağış Yap

**[☕️ Kahve Ismarla](https://KekikAkademi.org/Kahve)**

***

> **[@KekikAkademi](https://t.me/KekikAkademi)** *için yazılmıştır..*