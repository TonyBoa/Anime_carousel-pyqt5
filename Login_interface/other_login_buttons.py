from qt import *

class OtherLoginButtons(QPushButton):

    def __init__(self, icon: str, parent):
        super().__init__(parent)

        self.icon = QPixmap(icon)
        self.resize(54, 54)
        self.setCursor(Qt.PointingHandCursor)

    def paintEvent(self, a0):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setViewport(0, 0, self.width(), self.height())
        painter.setWindow(0, 0, self.width(), self.height())

        path = QPainterPath()
        path.addRoundedRect(0, 0, self.width(), self.height(), self.height()//4, self.height()//4)
        painter.setClipPath(path)
        painter.setPen(Qt.NoPen)

        pen = QPen()
        pen.setWidth(8)
        pen.setColor(QColor(220, 220, 220, 255))
        painter.setPen(pen)
        painter.drawRoundedRect(0, 0, self.width(), self.height(), self.height()//4, self.height()//4)

        rect = QRect(0, 0, self.width()//2, self.height()//2)
        rect.moveCenter(QPoint(self.width()//2, self.height()//2))
        painter.drawPixmap(rect, self.icon)

