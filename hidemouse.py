from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui, QtCore
import sys
import screenutils


width, height = screenutils.monitors[0].width, screenutils.monitors[0].height


class CursorHide(QMainWindow):
    def __init__(self):
        super(CursorHide, self).__init__()

        self.setFixedSize(width, height)
        self.move(0, 0)

        # hide cursor
        pm = QtGui.QPixmap('blank.png')
        cursor = QtGui.QCursor(pm)
        self.setCursor(cursor)

        # transparent window
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)


app = QApplication(sys.argv)
ex = CursorHide()


def show():
    ex.show()


def hide():
    ex.hide()


if __name__ == '__main__':
    main()
