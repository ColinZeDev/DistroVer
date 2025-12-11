from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QApplication
from backend import Backend

app = QApplication([])

backend = Backend()

engine = QQmlApplicationEngine()
engine.rootContext().setContextProperty("backend", backend)
engine.load("gui.qml")

print(
"""
+--------------------------------------------------------------+\n
|            Made by ColinZeDev on Github!                     |\n
|      Repo: https://github.com/ColinZeDev/DistroVer/          |\n
|                                                              |\n
|      !! THIS CODE IS UNDER THE GPL-3.0 LICENSE !!            |\n
|      !! PLEASE READ THE LICENSE FILE BEFORE MODIFYING !!     |\n
+--------------------------------------------------------------+
"""
)

app.exec()
