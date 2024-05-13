from PySide6.QtWidgets import QApplication
from mainwindow import mainWindow
import sys

app = QApplication(sys.argv)

Main = mainWindow()
Main.show()

app.exec()