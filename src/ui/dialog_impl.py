from .ui_base import dialog_edit
from PySide6 import QtCore, QtGui, QtWidgets


class NewDialog(dialog_edit.Ui_AddSourceDialog, QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

    def setupUi(self, AddSourceDialog):
        super().setupUi(AddSourceDialog)
        self.buttonBox.accepted.connect(self.add_btn_onClick)

    def add_btn_onClick(self):
        self.parent.add_app(
            self.bundleid_edit.text(),
            self.appname_edit.text(),
            self.version_edit.text(),
            self.itunes_edit.text(),
            self.download_edit.text(),
        )
        self.close()
