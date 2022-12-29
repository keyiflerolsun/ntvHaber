# 📰 ntvHaber

**Python Yazılımların Python ve Flatpak olarak Paketlenme Örneği**

_[@flet-dev](https://github.com/flet-dev) ile.._

## 🐍 Python Paketleme Örneği

```bash
# Paketle
pip install .

# Artıkları Temizle
rm -rf build/ dist/ *.egg-info/ .eggs/ && find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

# Çalıştır
ntvHaber

# Paketi Kaldır
pip uninstall ntvHaber
```

## 📦 Flatpak Paketleme Örneği

```bash
# Paketle
flatpak-builder --user --install --force-clean build-dir org.kekikakademi.ntvHaber.yml

# Artıkları Temizle
rm -rf .flatpak* .vscode build-dir && find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

# Çalıştır
flatpak run org.kekikakademi.ntvHaber

# Paketi Kaldır
flatpak uninstall org.kekikakademi.ntvHaber
```

## ⚠️ Bilinen Olumsuzluklar

- **Flet** varsayılan başlık ve ikonu henüz değişemiyor.
    - > https://github.com/flet-dev/flet/discussions/378
