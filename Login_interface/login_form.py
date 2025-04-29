import os.path

from qt import *
from Login_interface.input_box import *
from Login_interface.login_button import *
from Login_interface.other_login_buttons import *

class LoginForm(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.resize(477, 620)

        self.zoom_rate = 20

        username = InputBox(os.path.abspath("res/img/account.png"), self)
        username.move(46, 161)
        username.setPlaceholderText("Username")
        username.setMaxLength(11)
        username.setValidator(QIntValidator(0, 9999, self))

        password = InputBox(os.path.abspath("res/img/password.png"), self)
        password.move(46, 253)
        password.setPlaceholderText("Password")
        password.setEchoMode(QLineEdit.Password)
        password.setMaxLength(16)
        password.setValidator(QRegularExpressionValidator(QRegularExpression("[a-zA-Z0-9]+$"), self))

        self.login_button = LoginButton(self)
        self.login_button.set_center_text("Login")
        self.login_button.move(46, 371)

        other_login_buttons1 = OtherLoginButtons(os.path.abspath("res/img/logo_google.png"), self)
        other_login_buttons1.move(110, 480)

        other_login_buttons2 = OtherLoginButtons("res/img/facebook.png", self)
        other_login_buttons2.move(178, 480)

        other_login_buttons3 = OtherLoginButtons(os.path.abspath("res/img/github-fill.png"), self)
        other_login_buttons3.move(250, 480)

        other_login_buttons4 = OtherLoginButtons(os.path.abspath("res/img/instagram.png"), self)
        other_login_buttons4.move(320, 480)

        self.animations()
        self.login_button.execute_animation_signal.connect(self.execute_animation)

    def animations(self):
        self.animation = QPropertyAnimation(self.login_button, b"geometry")
        self.animation.setDuration(250)
        self.animation.setStartValue(self.login_button.geometry())
        self.animation.setEndValue(QRect(self.login_button.pos().x() + self.zoom_rate, self.login_button.pos().y() + self.zoom_rate // 2, self.login_button.width() - self.zoom_rate * 2, self.login_button.height() - self.zoom_rate))
        self.animation.setEasingCurve(QEasingCurve.Linear)

    def execute_animation(self, state):
        if state == LoginButton.Execute:
            self.animation.setDirection(QAbstractAnimation.Forward)
            self.animation.start()
        elif state == LoginButton.Restore:
            self.animation.setDirection(QAbstractAnimation.Backward)
            self.animation.start()


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.TextAntialiasing)
        painter.setViewport(0, 0, 477, 620)
        painter.setWindow(0, 0, 477, 620)

        self.crop_corner()
        self.draw_text()

    def crop_corner(self):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        brush = QBrush(QColor(255, 255, 255, 255))
        painter.setBrush(brush)
        painter.drawRect(0, 0, self.width(), self.height())

    def draw_text(self):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.TextAntialiasing)

        rect1 = QRect (0, 0, 0, 0)
        font1 = QFont()
        font1.setPointSize(30)
        font1.setBold(True)
        font1.setWordSpacing(1)
        painter.setFont(font1)

        semiTransparent = QColor(0, 0, 0, 255)
        painter.setPen(semiTransparent)

        actualRect = painter.boundingRect(rect1, Qt.AlignCenter, "Login")
        rect1.setHeight(actualRect.height())
        rect1.setWidth(actualRect.width())
        rect1.moveCenter(QPoint(self.width() // 2, self.height() // 6))
        painter.drawText(rect1, 0, "Login")
