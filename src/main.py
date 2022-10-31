from ui import interface_impl
from PySide6 import QtCore, QtGui, QtWidgets
import sys


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = interface_impl.SourceInterface()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

    pass


if __name__ == "__main__":
    main()
