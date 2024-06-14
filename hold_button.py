from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QTimer, Signal, Qt

class HoldButton(QPushButton):
    holdPressed = Signal()
    holdReleased = Signal()
    clicked = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._hold_timer = QTimer(self)
        self._hold_timer.setSingleShot(True)
        self._hold_timer.timeout.connect(self.on_hold)
        self._is_holding = False
        self._hold_duration = 1000  # Duration in milliseconds

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._hold_timer.start(self._hold_duration)
            self._is_holding = True
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self._is_holding:
                self._hold_timer.stop()
                if not self._hold_timer.isActive():
                    self.on_click()
                else:
                    self.holdReleased.emit()
                self._is_holding = False
        super().mouseReleaseEvent(event)

    def on_hold(self):
        if self._is_holding:
            self._is_holding = False
            self.holdPressed.emit()

    def on_click(self):
        self.clicked.emit()
