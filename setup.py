# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from setuptools import setup
from io         import open

setup(
    # ? Genel Bilgiler
    name         = "ntvHaber",
    version      = "0.6",
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
        "pip",
        "setuptools",
        "wheel",
        "rich",
        "flet",
        "notify-py",
        "requests"
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
        ("share/applications",                ["org.kekikakademi.ntvHaber.desktop"]),
        ("share/appdata",                     ["org.kekikakademi.ntvHaber.appdata.xml"]),
        ("share/icons/hicolor/scalable/apps", ["ntvHaber/Assets/Logo.png"])
    ],

    # ? PyPI Bilgileri
    long_description_content_type = "text/markdown",
    long_description              = "".join(open("PyPi.md", encoding="utf-8").readlines()),
    include_package_data          = True
)