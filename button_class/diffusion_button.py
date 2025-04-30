from qt import *

class DiffusionButton(QPushButton):
    radiusChanged = pyqtSignal()
    opacityChanged = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setCursor(Qt.PointingHandCursor)
        self.resize(130, 42)

        self.m_radius = 0
        self.m_opacity = 255

        self.mouse_coordinates = QPoint()

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setOffset(0, 16)
        shadow.setBlurRadius(50)
        shadow.setColor(QColor(0, 0, 0, 166))
        self.setGraphicsEffect(shadow)

        self.animation3 = QPropertyAnimation(self, b"radius")
        self.animation3.setDuration(400)
        self.animation3.setStartValue(self.m_radius)
        self.animation3.setEndValue(self.width())
        self.animation3.setEasingCurve(QEasingCurve.Linear)
        self.animation3.setDirection(QAbstractAnimation.Forward)

        self.animation1 = QPropertyAnimation(self, b"opacity")
        self.animation1.setDuration(400)
        self.animation1.setStartValue(self.m_opacity)
        self.animation1.setEndValue(0)
        self.animation1.setEasingCurve(QEasingCurve.Linear)
        self.animation1.setDirection(QAbstractAnimation.Forward)

        self.animation3.finished.connect(self.reset_animation)
        self.animation1.finished.connect(self.reset_animation)

    def draw_disappearing_circle(self):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        brush = QBrush(QColor(135, 206, 235, self.m_opacity))
        painter.setBrush(brush)
        painter.drawEllipse(self.mouse_coordinates, self.m_radius, self.m_radius)

    def execute_animation(self):
        self.animation3.start()
        self.animation1.start()

    def reset_animation(self):
        self.m_radius = 0
        self.m_opacity = 255

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setViewport(0, 0, self.width(), self.height())
        painter.setWindow(0, 0, self.width(), self.height())

        path = QPainterPath()
        path.addRoundedRect(0, 0, self.width(), self.height(), 21, 21)
        painter.setClipPath(path)
        painter.setPen(Qt.NoPen)

        brush = QBrush(QColor(255, 255, 255, 255))
        painter.setBrush(brush);
        painter.drawRect(0, 0, self.width(), self.height())
        self.draw_disappearing_circle()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_coordinates = event.pos()
            self.update()
            self.execute_animation()

    def radius(self):
        return self.m_radius;

    def setRadius(self, newRadius):
        if self.m_radius == newRadius:
            return
        self.m_radius = newRadius
        self.update()
        self.radiusChanged.emit()

    radius = pyqtProperty(int, radius, setRadius, notify=radiusChanged)

    def opacity(self):
        return self.m_opacity

    def setOpacity(self, newOpacity):
        if self.m_opacity == newOpacity:
            return
        self.m_opacity = newOpacity
        self.update()
        self.opacityChanged.emit()

    opacity = pyqtProperty(int, opacity, setOpacity, notify=opacityChanged)

