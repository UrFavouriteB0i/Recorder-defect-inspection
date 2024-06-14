from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QImage, QPixmap, QPainter, QBrush, QColor, QPen
from PySide6.QtCore import Qt, QRect, QPoint, Signal

class Labelimage(QLabel):
    roi_selected = Signal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(9,9,640,480)
        self.begin = QPoint()
        self.end = QPoint()
        self.current_rect = QRect()
        self.X = 0
        self.Y = 0
        self.WIDTH = 0
        self.HEIGHT = 0 

    def paintEvent(self, event):
        super().paintEvent(event)
        qp = QPainter(self)
        try:
            qp.setBrush(QColor(255,255,255,40))
            qp.setPen(Qt.darkRed)
            qp.setPen(Qt.DashLine)
            
            # Draw the current rectangle being drawn
            qp.drawRect(QRect(self.begin, self.end))
            # Draw the saved rectangle
            qp.drawRect(self.current_rect)
        finally:
            qp.end()

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = event.pos()
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        # super(Labelimage, self).mouseReleaseEvent(event)
        self.end = event.pos()
        self.current_rect = QRect(self.begin, self.end).normalized()
        self.update()
        self.X, self.Y, self.WIDTH, self.HEIGHT = self.current_rect.x(), self.current_rect.y(), self.current_rect.width(), self.current_rect.height()

        X = self.roundVAL(self.X, 2)
        Y = self.roundVAL(self.Y, 2)
        W = self.roundVAL(self.WIDTH, 16)
        H = self.roundVAL(self.HEIGHT, 4)
        
        self.X, self.Y, self.WIDTH, self.HEIGHT = self.rescale_frame(X, Y, W, H)
        
        self.roi_selected.emit(True)

    def roundVAL(self,val, multi):
        remainder = val % multi

        if remainder == 0: return val
        
        lower = val - remainder
        upper = lower + multi

        if (val-lower)<(upper-val): return lower

        else: return upper

    def rescale_frame(self, x,y,w,h):
        ori_w, ori_h = 1280, 1024
        resize_w, resize_h = 640, 480

        scale_x = ori_w / resize_w
        scale_y = ori_h / resize_h

        roi_x = int(x * scale_x)
        roi_y = int(y * scale_y)
        roi_w = int(w * scale_x)
        roi_h = int(h * scale_y)

        return roi_x, roi_y, roi_w, roi_h