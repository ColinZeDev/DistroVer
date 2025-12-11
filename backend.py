from PySide6.QtCore import QObject, Property
import subprocess
import distro
import json
import os

with open('imgs.json', 'r') as f:
    DISTRO_IMGS = json.load(f)

DEFAULT_IMG = "img/linux.png"


def get_distro_logo():
    distro_id = distro.id().lower()

    if distro_id in DISTRO_IMGS:
        return DISTRO_IMGS[distro_id]

    for like in distro.like().split():
        if like.lower() in DISTRO_IMGS:
            return DISTRO_IMGS[like.lower()]

    return DEFAULT_IMG


class Backend(QObject):
    def __init__(self):
        super().__init__()

        name = distro.name()
        version = distro.version()
        codename = distro.codename() or "[Unknown]"
        hostname = os.uname().nodename
        username = os.environ.get("USER") or os.environ.get("USERNAME")
        kernel = subprocess.check_output(['uname', '-r']).decode()

        self._logo = get_distro_logo()

        self._info = (
            f"{name}\n\n"
            f"Version {version} ({codename})\n\n"
            f"Host name: {hostname}\n\n"
            f"Username: {username}\n\n"
            f"Kernel: {kernel}\n\n"
        )

        self._version = "0.0.2"

    @Property(str, constant=True)
    def logo(self):
        return self._logo

    @Property(str, constant=True)
    def infoText(self):
        return self._info

    @Property(str, constant=True)
    def version(self):
        return self._version
