from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QApplication
from backend import Backend

app = QApplication([])

backend = Backend()

engine = QQmlApplicationEngine()
engine.rootContext().setContextProperty("backend", backend)
engine.load("gui.qml")

app.exec()
