# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from setuptools import setup
from io         import open

setup(
    # ? Genel Bilgiler
    name         = "ntvHaber",
    version      = "1.30.0",
    url          = "https://github.com/keyiflerolsun/ntvHaber",
    description  = "NTV Son Dakika Haberleri",
    keywords     = ["ntvHaber", "KekikAkademi", "keyiflerolsun"],

    author       = "keyiflerolsun",
    author_email = "keyiflerolsun@gmail.com",

    license      = "GPLv3+",
    classifiers  = [
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3"
    ],

    # ? Paket Bilgileri
    packages         = ["ntvHaber"],
    python_requires  = ">=3.10",
    install_requires = [
        "setuptools",
        "wheel",
        "install-freedesktop",
        "rich",
        "flet",
        "pystray",
        "Pillow",
        "notify-py",
        "requests",
        "APScheduler",
        "parsel"
    ],

    # ? Konsoldan Çalıştırılabilir
    entry_points = {
        "console_scripts": [
            "ntvHaber = ntvHaber:basla",
        ]
    },

    # ? Masaüstü Paketi
    setup_requires = ["install_freedesktop"],
    data_files     = [
        ("share/applications",                ["Shared/org.kekikakademi.ntvHaber.desktop"]),
        ("share/appdata",                     ["Shared/org.kekikakademi.ntvHaber.appdata.xml"]),
        ("share/icons/hicolor/scalable/apps", ["Shared/org.kekikakademi.ntvHaber.svg"])
    ],

    # ? PyPI Bilgileri
    long_description_content_type = "text/markdown",
    long_description              = "".join(open("README.md", encoding="utf-8").readlines()),
    include_package_data          = True
)