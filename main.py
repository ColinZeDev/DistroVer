from tkinter import ttk
import tkinter as tk
import platform
import distro
import os

VERSION = "0.0.1"

DISTRO_IMGS = { # I will add more when I'm not lazy
    "debian": os.path.join('img', 'debian.gif'),
    "arch": os.path.join('img', 'arch.gif'),
    "ubuntu": os.path.join('img', 'ubuntu.gif'),
    "fedora": os.path.join('img', 'fedora.gif'),
    "rhel": os.path.join('img', 'rhel.gif'),
    "opensuse": os.path.join('img', 'opensuse.gif'),
    "gentoo": os.path.join('img', 'gentoo.gif'),
    "linuxmint": os.path.join('img', 'linuxmint.gif'),
    "pidora": os.path.join('img', 'pidora.gif'),
    "raspbian": os.path.join('img', 'raspbian.gif'),
    "rocky": os.path.join('img', 'rocky.gif'),
    "nixos": os.path.join('img', 'nixos.gif'),
    "kali": os.path.join('img', 'kali.gif')
}
DEFAULT_IMG = "img/linux.gif"


def get_distro_logo():
    distro_id = distro.id().lower()

    if distro_id in DISTRO_IMGS:
        return DISTRO_IMGS[distro_id]

    like_ids = distro.like().lower().split()

    for like in like_ids:
        if like in DISTRO_IMGS:
            return DISTRO_IMGS[like]

    return DEFAULT_IMG


class Main:
    def __init__(self):
        self.root = tk.Tk()
        self.make_geo(483, 509)
        self.root.title(f"DistroVer v{VERSION}")
        self.root.resizable(False, False)

        #self.root.bind("<Configure>", self.on_resize)

        self.build_ui()

    def make_geo(self, w: int, h: int, offset_x: int = 20, offset_y: int = 20):
        self.root.update_idletasks()
        x = self.root.winfo_screenwidth() - w - offset_x
        y = offset_y
        self.root.geometry(f"{w}x{h}+{x}+{y}")

    def build_ui(self):
        name = distro.name()

        frame = ttk.Frame(self.root, padding=20)
        frame.pack(fill="both", expand=True)

        top = ttk.Frame(frame)
        top.pack(fill="x", pady=(0, 15))

        logo_path = get_distro_logo()
        self.logo_tk = tk.PhotoImage(file=logo_path)

        logo_label = tk.Label(top, image=self.logo_tk)
        logo_label.grid(row=0, column=0)

        top.grid_columnconfigure(0, weight=1)

        sep = ttk.Separator(frame, orient="horizontal")
        sep.pack(fill="x", pady=10)

        center = ttk.Frame(frame)
        center.pack(fill="x", pady=(10, 10))

        version = distro.version()
        codename = distro.codename() or "[Unknown]"
        hostname = os.uname().nodename
        username = os.environ.get("USER") or os.environ.get("USERNAME")

        info_text = (
            f"{name}\n\n"
            f"Version {version} ({codename})\n\n"
            f"Host name: {hostname}\n\n"
            f"Username: {username}\n\n"
            f"Kernel: {platform.release()}\n\n"
        )

        info_label = tk.Label(
            center,
            text=info_text,
            font=("Segoe UI", 11),
            justify="center"
        )
        info_label.pack()

    def run(self, n: int = 0):
        self.root.mainloop(n)

    def on_resize(self, event):
        print(f"Window size → {event.width}x{event.height}")


if __name__ == "__main__":
    main = Main()
    main.run()