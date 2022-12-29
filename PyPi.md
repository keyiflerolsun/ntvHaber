# 📰 ntvHaber

![Repo Boyutu](https://img.shields.io/github/repo-size/keyiflerolsun/ntvHaber)
![Görüntülenme](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://github.com/keyiflerolsun/ntvHaber&title=Görüntülenme)
<a href="https://KekikAkademi.org/Kahve" target="_blank"><img src="https://img.shields.io/badge/☕️-Kahve Ismarla-ffdd00" title="☕️ Kahve Ismarla" style="padding-left:5px;"></a>
[![AppVeyor](https://ci.appveyor.com/api/projects/status/o1351onjr97789ea?svg=true)](https://ci.appveyor.com/project/keyiflerolsun/ntvHaber)

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ntvHaber)
![PyPI - Status](https://img.shields.io/pypi/status/ntvHaber)
![PyPI](https://img.shields.io/pypi/v/ntvHaber)
![PyPI - Downloads](https://img.shields.io/pypi/dm/ntvHaber)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/ntvHaber)
![PyPI - License](https://img.shields.io/pypi/l/ntvHaber)

**Python Yazılımların Python ve Flatpak olarak Paketlenme Örneği**

_[@flet-dev](https://github.com/flet-dev) ile.._

[![ForTheBadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/keyiflerolsun/)

## 🚀 Doğrudan Kullanım

```bash
git clone https://github.com/keyiflerolsun/ntvHaber.git
cd ntvHaber

pip install -Ur requirements.txt

python basla.py
```

## <img src="https://www.akashtrehan.com/assets/images/emoji/terminal.png" height="42" align="center"> Manuel Paketleme Seçenekleri

### 🐍 Python

```bash
git clone https://github.com/keyiflerolsun/ntvHaber.git
cd ntvHaber
git checkout paketlenebilir

# Paketle
pip install .

# Artıkları Temizle
rm -rf build/ dist/ *.egg-info/ .eggs/ && find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

# Çalıştır
ntvHaber

# Paketi Kaldır
pip uninstall ntvHaber
```

### 📦 Flatpak

```bash
git clone https://github.com/keyiflerolsun/ntvHaber.git
cd ntvHaber
git checkout paketlenebilir

# Paketle
flatpak-builder --user --install --force-clean build-dir org.kekikakademi.ntvHaber.yml

# Artıkları Temizle
rm -rf .flatpak* .vscode build-dir && find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

# Çalıştır
flatpak run org.kekikakademi.ntvHaber

# Paketi Kaldır
flatpak uninstall org.kekikakademi.ntvHaber
```

### ⚠️ Bilinen Olumsuzluklar

- **Flet** varsayılan başlık ve ikonu henüz değişemiyor.
    - > https://github.com/flet-dev/flet/discussions/378


## 💸 Bağış Yap

**[☕️ Kahve Ismarla](https://KekikAkademi.org/Kahve)**

## 🌐 Telif Hakkı ve Lisans

* *Copyright (C) 2022 by* [keyiflerolsun](https://github.com/keyiflerolsun) ❤️️
* [GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007](https://github.com/keyiflerolsun/ntvHaber/blob/master/LICENSE) *Koşullarına göre lisanslanmıştır..*

## ♻️ İletişim

*Benimle iletişime geçmek isterseniz, **Telegram**'dan mesaj göndermekten çekinmeyin;* [@keyiflerolsun](https://t.me/KekikKahve)

##

> **[@KekikAkademi](https://t.me/KekikAkademi)** *için yazılmıştır..*
