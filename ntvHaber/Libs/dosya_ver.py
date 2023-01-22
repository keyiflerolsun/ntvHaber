# https://github.com/jellyfin/jellyfin-mpv-shim/blob/master/jellyfin_mpv_shim/utils.py#L239

import os, sys, platform

def get_resource(*path):
    # Detect if bundled via pyinstaller.
    # From: https://stackoverflow.com/questions/404744/
    if getattr(sys, "_MEIPASS", False):
        application_path = os.path.join(getattr(sys, "_MEIPASS"), "ntvHaber")
    else:
        application_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # ! Test code for Mac
    if getattr(sys, "frozen", False) and platform.system() == "Darwin":
        application_path = os.path.join(os.path.dirname(os.path.dirname(sys.executable)), "../Resources")

    return os.path.join(application_path, *path)