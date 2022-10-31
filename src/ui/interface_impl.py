from .ui_base import interface
from . import dialog_impl
from PySide6 import QtCore, QtGui, QtWidgets
import json
from data.ipa_source_format import IPASourceFormat


class SourceInterface(interface.Ui_SourceMainWindow):
    def __init__(self):
        super().__init__()

    @property
    def app_list(self):
        if not hasattr(self, "_app_list"):
            self._app_list = []
        return self._app_list

    @app_list.setter
    def app_list(self, value: list):
        self._app_list = value
        self.update_table()

    def setupUi(self, SourceMainWindow):
        super().setupUi(SourceMainWindow)
        self.actionNew.triggered.connect(self.new_commandLinkButton_onClick)
        self.actionOpen_Database.triggered.connect(self.open_btn_onClick)
        self.actionSave_Database.triggered.connect(self.save_commandLinkButton_onClick)
        self.actionExit.triggered.connect(SourceMainWindow.close)
        self.Button_Add.clicked.connect(self.add_btn_onClick)
        self.Button_Remove.clicked.connect(self.remove_btn_onClick)
        self.actionAdd_Item.triggered.connect(self.add_btn_onClick)
        self.actionRemove_Item.triggered.connect(self.remove_btn_onClick)
        self.AppsTable.cellChanged.connect(self.table_edit)

    def new_commandLinkButton_onClick(self):
        # Make a new blank database
        self.app_list = []

    def open_btn_onClick(self):
        # Open a file selection dialog
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFile)
        dialog.setNameFilter("JSON Files (*.json)")
        dialog.setViewMode(QtWidgets.QFileDialog.ViewMode.Detail)
        if dialog.exec():
            # Load the file
            with open(dialog.selectedFiles()[0], "r") as file:
                self.app_list = json.load(file, object_hook=IPASourceFormat.from_json)

            # Update the table
            self.update_table()

    def update_table(self):
        # Temporary disable the table edit event
        self.AppsTable.cellChanged.disconnect()

        # Update the table
        self.AppsTable.setRowCount(len(self.app_list) + 1)
        self.AppsTable.setColumnCount(5)

        # Stretch columns to fit the table
        self.AppsTable.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Stretch
        )

        for i, app in enumerate(self.app_list):
            self.AppsTable.setItem(i, 0, QtWidgets.QTableWidgetItem(app.bundleID))
            self.AppsTable.setItem(i, 1, QtWidgets.QTableWidgetItem(app.name))
            self.AppsTable.setItem(i, 2, QtWidgets.QTableWidgetItem(app.version))
            self.AppsTable.setItem(i, 3, QtWidgets.QTableWidgetItem(app.itunesLookup))
            self.AppsTable.setItem(i, 4, QtWidgets.QTableWidgetItem(app.link))

        for i in range(5):
            self.AppsTable.setItem(
                len(self.app_list), i, QtWidgets.QTableWidgetItem("")
            )

        # Re-enable the table edit event
        self.AppsTable.cellChanged.connect(self.table_edit)

    def add_btn_onClick(self):
        # Open the new app dialog
        self.new_app_dialog = QtWidgets.QDialog()
        self.new_app_dialog_ui = dialog_impl.NewDialog(parent=self)
        self.new_app_dialog_ui.setupUi(self.new_app_dialog)
        self.new_app_dialog.setModal(True)
        self.new_app_dialog.show()

    def add_app(self, bundleID, name, version, itunesLookup, link):
        # Add the app
        # print(bundleID, name, version, itunesLookup, link)
        if not self.app_list:
            self.app_list = []

        self.app_list = self.app_list + [
            IPASourceFormat(bundleID, name, version, itunesLookup, link)
        ]

    def remove_btn_onClick(self):
        # If nothing is selected, return
        if self.AppsTable.currentRow() == -1:
            return
        # Remove the selected app from the list
        self.app_list.pop(self.AppsTable.currentRow())

    def table_edit(self, row, column):
        # If the index don't exist, create it
        if len(self.app_list) <= row:
            self.app_list = self.app_list + [
                IPASourceFormat(
                    self.AppsTable.item(row, 0).text(),
                    self.AppsTable.item(row, 1).text(),
                    self.AppsTable.item(row, 2).text(),
                    self.AppsTable.item(row, 3).text(),
                    self.AppsTable.item(row, 4).text(),
                )
            ]
            return

        # Update the item
        self.app_list[row] = IPASourceFormat(
            self.AppsTable.item(row, 0).text(),
            self.AppsTable.item(row, 1).text(),
            self.AppsTable.item(row, 2).text(),
            self.AppsTable.item(row, 3).text(),
            self.AppsTable.item(row, 4).text(),
        )

    def save_commandLinkButton_onClick(self):
        # Open a file selection dialog
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.FileMode.AnyFile)
        dialog.setNameFilter("JSON Files (*.json)")
        dialog.setViewMode(QtWidgets.QFileDialog.ViewMode.Detail)
        dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptMode.AcceptSave)
        if dialog.exec():
            # Save the file
            with open(dialog.selectedFiles()[0], "w") as file:
                json.dump(
                    self.app_list, file, indent=4, cls=IPASourceFormat.JSONEncoder
                )

    def exit_commandLinkButton_onClick(self):
        # Close the window
        self.close()
