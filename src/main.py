from ui import interface_impl
from PySide6 import QtCore, QtGui, QtWidgets
import sys


def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = interface_impl.SourceInterface()
    mainWindow.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec())

    pass


if __name__ == "__main__":
    main()
