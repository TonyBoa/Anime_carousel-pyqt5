from qt import *
from math import sqrt

class WaveButton(QPushButton):
    angleChanged = pyqtSignal()
    wave_positionChanged = pyqtSignal()
    wave_transparencyChanged = pyqtSignal()
    right_angleChanged = pyqtSignal()

    def __init__(self, parent):
        super().__init__(parent)
        self.resize(147, 55)
        self.setCursor(Qt.PointingHandCursor)

        self.m_angle = 25
        self.m_right_angle = 1080
        self.m_wave_position = 0
        self.m_wave_transparency = 100

        self.m_wave_position = int(sqrt(pow(self.width(), 2) + pow(self.width(), 2)) // 2)
        self.execution_time = 4000
        self.click_status = True

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setOffset(0, 16)
        shadow.setBlurRadius(50)
        shadow.setColor(QColor(0, 0, 0, 255))
        self.setGraphicsEffect(shadow)

    def triangle_position(self):
        return sqrt(pow(self.width(), 2) + pow(self.width(), 2)) // 2

    def rotating_rounded_rectangle(self):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        path = QPainterPath()
        path.addRoundedRect(0, 0, self.width(), self.height(), 26, 26)
        painter.setClipPath(path)

        color = QColor(0, 0, 222, self.m_wave_transparency)

        rect = QRect(0 - self.width() // 5 * 4, self.m_wave_position, self.width() * 2, self.width() * 2)
        painter.translate(rect.center())
        painter.rotate(self.m_angle)
        painter.setPen(Qt.NoPen)
        painter.setBrush(color)
        painter.drawRoundedRect(-rect.width() // 2, -rect.height() // 2, rect.width(), rect.height(), self.width() * 0.9, self.width() * 0.9)

    def rotating_rounded_rectangle1(self):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        path = QPainterPath()
        path.addRoundedRect(0, 0, self.width(), self.height(), 26, 26)
        painter.setClipPath(path)

        color = QColor(0, 0, 222, self.m_wave_transparency)

        rect1 = QRect(0 - self.width() // 20, self.m_wave_position, self.width() * 2, self.width() * 2)
        painter.translate(rect1.center())
        painter.rotate(self.m_right_angle)
        painter.setPen(Qt.NoPen)
        painter.setBrush(color)
        painter.drawRoundedRect(-rect1.width() // 2, -rect1.height() // 2, rect1.width(), rect1.height(), self.width() * 0.9, self.width() * 0.9)

    def draw_border(self):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        path = QPainterPath()
        path.addRoundedRect(0, 0, self.width(), self.height(), 26, 26)
        painter.setClipPath(path)

        pen = QPen()
        pen.setWidth(8)
        pen.setColor(QColor(0, 0, 255, 255))
        painter.setPen(pen)
        painter.drawRoundedRect(0, 0, self.width(), self.height(), 26, 26)

    def draw_text(self):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.TextAntialiasing)
        painter.setViewport(0, 0, self.width(), self.height())
        painter.setWindow(0, 0, self.width(), self.height())

        rect1 = QRect(0, 0, self.width(), self.height())

        font1 = QFont()
        font1.setPointSize(13)
        font1.setLetterSpacing(QFont.AbsoluteSpacing, 2)

        font1.setBold(True)
        painter.setFont(font1)
        semiTransparent = QColor(255, 255, 255, 255)
        painter.setPen(semiTransparent)
        painter.drawText(rect1, Qt.AlignCenter, "Click")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setViewport(0, 0, self.width(), self.height())
        painter.setWindow(0, 0, self.width(), self.height())

        self.rotating_rounded_rectangle()

        self.rotating_rounded_rectangle1()

        self.draw_border()

        self.draw_text()

    def execute_animation(self):
        self.animation1 = QPropertyAnimation(self, b"angle")
        self.animation1.setDuration(self.execution_time)
        self.animation1.setStartValue(self.m_angle)
        self.animation1.setEndValue(1080)
        self.animation1.setEasingCurve(QEasingCurve.Linear)
        self.animation1.start(QAbstractAnimation.DeleteWhenStopped)

        self.animation4 = QPropertyAnimation(self, b"right_angle")
        self.animation4.setDuration(self.execution_time)
        self.animation4.setStartValue(self.m_right_angle)
        self.animation4.setEndValue(25)
        self.animation4.setEasingCurve(QEasingCurve.Linear)
        self.animation4.start(QAbstractAnimation.DeleteWhenStopped)

        self.animation2 = QPropertyAnimation(self, b"wave_position")
        self.animation2.setDuration(self.execution_time)
        self.animation2.setStartValue(self.m_wave_position)
        self.animation2.setEndValue(-self.height())
        self.animation2.setEasingCurve(QEasingCurve.Linear)
        self.animation2.start(QAbstractAnimation.DeleteWhenStopped)

        self.animation3 = QPropertyAnimation(self, b"wave_transparency")
        self.animation3.setDuration(self.execution_time)
        self.animation3.setStartValue(self.m_wave_transparency)
        self.animation3.setEndValue(255)
        self.animation3.setEasingCurve(QEasingCurve.Linear)
        self.animation3.start(QAbstractAnimation.DeleteWhenStopped)

    def restore_animation(self):
        self.animation1 = QPropertyAnimation(self, b"angle")
        self.animation1.setDuration(self.execution_time)
        self.animation1.setStartValue(self.m_angle)
        self.animation1.setEndValue(25)
        self.animation1.setEasingCurve(QEasingCurve.Linear)
        self.animation1.start(QAbstractAnimation.DeleteWhenStopped)

        self.animation4 = QPropertyAnimation(self, b"right_angle")
        self.animation4.setDuration(self.execution_time)
        self.animation4.setStartValue(self.m_right_angle)
        self.animation4.setEndValue(1080)
        self.animation4.setEasingCurve(QEasingCurve.Linear)
        self.animation4.start(QAbstractAnimation.DeleteWhenStopped)

        self.animation2 = QPropertyAnimation(self, b"wave_position")
        self.animation2.setDuration(self.execution_time)
        self.animation2.setStartValue(self.m_wave_position)
        self.animation2.setEndValue(self.triangle_position())
        self.animation2.setEasingCurve(QEasingCurve.Linear)
        self.animation2.start(QAbstractAnimation.DeleteWhenStopped)

        self.animation3 = QPropertyAnimation(self, b"wave_transparency")
        self.animation3.setDuration(self.execution_time)
        self.animation3.setStartValue(self.m_wave_transparency)
        self.animation3.setEndValue(100)
        self.animation3.setEasingCurve(QEasingCurve.Linear)
        self.animation3.start(QAbstractAnimation.DeleteWhenStopped)


    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            if self.click_status:
                self.execute_animation()
                self.click_status = False
            else:
                self.restore_animation()
                self.click_status = True

    def angle(self):
        return self.m_angle

    def setAngle(self, newAngle):
        if self.m_angle == newAngle:
            return
        self.m_angle = newAngle
        self.update()
        self.angleChanged.emit()

    angle = pyqtProperty(int, angle, setAngle, notify=angleChanged)

    def wave_position(self):
        return self.m_wave_position

    def setWave_position(self, newWave_position):
        if self.m_wave_position == newWave_position:
            return
        self.m_wave_position = newWave_position
        self.update()
        self.wave_positionChanged.emit()

    wave_position = pyqtProperty(int, wave_position, setWave_position, notify=wave_positionChanged)

    def wave_transparency(self):
        return self.m_wave_transparency

    def setWave_transparency(self, newWave_transparency):
        if self.m_wave_transparency == newWave_transparency:
            return
        self.m_wave_transparency = newWave_transparency
        self.update()
        self.wave_transparencyChanged.emit()

    wave_transparency = pyqtProperty(int, wave_transparency, setWave_transparency, notify=wave_transparencyChanged)

    def right_angle(self):
        return self.m_right_angle

    def setRight_angle(self, newRight_angle):
        if self.m_right_angle == newRight_angle:
            return
        self.m_right_angle = newRight_angle
        self.update()
        self.right_angleChanged.emit()

    right_angle = pyqtProperty(int, right_angle, setRight_angle, notify=right_angleChanged)
