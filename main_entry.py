import sys
from Login_interface import *

if __name__ == '__main__':
    app = QApplication([])
    m = LoginForm(None)
    m.show()
    sys.exit(app.exec())