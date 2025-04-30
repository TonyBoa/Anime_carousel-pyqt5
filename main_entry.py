import sys
from Login_interface import *
from button_class import *

class MainForm(QWidget):

    def __init__(self):
        super().__init__()

        self.wave_button = WaveButton(self)
        self.wave_button.show()

        self.diffusion_button = DiffusionButton(self)
        self.diffusion_button.show()

        self.update_pos()

        self.resize(400, 400)

    def update_pos(self):
        left_rect = QRect(0, 0, self.rect().width()//2, self.rect().height())

        right_rect = QRect(self.width()//2, 0, self.rect().width()//2, self.rect().height())

        rect = self.wave_button.rect()
        rect.moveCenter(left_rect.center())
        self.wave_button.move(rect.topLeft())

        rect2 = self.diffusion_button.rect()
        rect2.moveCenter(right_rect.center())
        self.diffusion_button.move(rect2.topLeft())

    def resizeEvent(self, a0):
        self.update_pos()


if __name__ == '__main__':
    app = QApplication([])
    #m = LoginForm(None)
    m = MainForm()
    m.show()
    sys.exit(app.exec())