import sys
from PyQt6.QtWidgets import QApplication
from interface import YelCir


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YelCir()
    ex.show()
    sys.exit(app.exec())