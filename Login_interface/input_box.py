from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class InputBox(QLineEdit):

    def __init__(self, icon: str, parent):
        super().__init__(parent)

        self.icon = QPixmap(icon)
        self.resize(388, 58)

        self.setTextMargins(25, 0, 50, 0)

        font = self.font()
        font.setPointSize(15)
        self.setFont(font)

        palette = self.palette()
        palette.setColor(QPalette.PlaceholderText, Qt.gray)
        self.setPalette(palette)

        palette.setColor(QPalette.Text, Qt.black)
        self.setPalette(palette)

        palette.setColor(QPalette.Base, Qt.transparent)
        self.setPalette(palette)

        self.setFrame(False)

    def paintEvent(self, a0):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setViewport(0, 0, self.width(), self.height())
        painter.setWindow(0, 0, self.width(), self.height())

        self.crop_corner()
        self.draw_ico_image()
        super().paintEvent(a0)

    def crop_corner(self):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        path = QPainterPath()
        path.addRoundedRect(0, 0, self.width(), self.height(), 10, 10)
        painter.setClipPath(path)
        painter.setPen(Qt.NoPen)
        brush = QBrush(QColor(238, 238, 238, 255))
        painter.setBrush(brush)
        painter.drawRect(0, 0, self. width(), self.height())

    def draw_ico_image(self):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)

        rect = QRect(int(self.width() * 0.85), self.height()//4, self.height()//2, self.height()//2)
        painter.drawPixmap(rect, self.icon)

