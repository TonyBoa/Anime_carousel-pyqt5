from qt import *

class LoginButton(QPushButton):
    execute_animation_signal = pyqtSignal(int)

    Execute = 0
    Restore = 1

    def __init__(self, parent):
        super().__init__(parent)
        self.m_color_opacity = 255
        self.m_center_text = ""

        self.resize(392, 57)
        self.setCursor(Qt.PointingHandCursor)
        self.setMouseTracking(True)
        self.start_animation()

    def start_animation(self):
        self.ani = QPropertyAnimation(self, b'color_opacity')
        self.ani.setDuration(200)
        self.ani.setStartValue(self.m_color_opacity)
        self.ani.setEndValue(188)
        self.ani.setEasingCurve(QEasingCurve.Linear)

    def paintEvent(self, a0):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setViewport(0, 0, self.width(), self.height())
        painter.setWindow(0, 0, self.width(), self.height())

        path = QPainterPath()
        path.addRoundedRect(0, 0, self.width(), self.height(), 10, 10)
        painter.setClipPath(path)
        painter.setPen(Qt.NoPen)

        brush = QBrush(QColor(123, 150, 228, self.m_color_opacity))
        painter.setBrush(brush)
        painter.drawRect(0, 0, self.width(), self.height())

        self.draw_text()

    def draw_text(self):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.TextAntialiasing)

        rect1 = QRect(0, 0, 0, 0)
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        font1.setWordSpacing(1)
        painter.setFont(font1)

        semiTransparent = QColor(255, 255, 255, 255)
        painter.setPen(semiTransparent)

        font_metrics = QFontMetrics(painter.font())
        text_rect = font_metrics.boundingRect(self.m_center_text)

        actual_rect = painter.boundingRect(rect1, Qt.AlignCenter, self.m_center_text)
        rect1.setHeight(actual_rect.height())
        rect1.setWidth(actual_rect.width())
        rect1.moveCenter(QPoint(self.width() // 2, self.height() // 2))
        painter.drawText(rect1, 0, self.m_center_text)

    def color_opacity(self):
        return self.m_color_opacity

    def set_color_opacity(self, color_opacity):
        self.m_color_opacity = color_opacity
        self.update()

    color_opacity = pyqtProperty(int, color_opacity, set_color_opacity)

    def center_text(self):
        return self.m_center_text

    def set_center_text(self, text):
        self.m_center_text = text

    def event(self, a0):
        if a0.type() == QEvent.Enter:
            self.ani.setDuration(QPropertyAnimation.Forward)
            self.ani.start()
        elif a0.type() == QEvent.Leave:
            self.ani.setDuration(QPropertyAnimation.Backward)
            self.ani.start()
            self.update()
        return super().event(a0)

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.execute_animation_signal.emit(LoginButton.Execute)
        super().mousePressEvent(e)

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.execute_animation_signal.emit(LoginButton.Restore)
        super().mouseReleaseEvent(e)


