import sys
from Login_interface import *
from button_class import *

class MainForm(QWidget):

    def __init__(self):
        super().__init__()

        self.resize(400, 400)

        m = WaveButton(self)
        m.show()

        m.move(self.width()//2 - m.width()//2, self.height()//2 - m.height()//2)
        m.raise_()

if __name__ == '__main__':
    app = QApplication([])
    #m = LoginForm(None)
    m = MainForm()
    m.show()
    sys.exit(app.exec())