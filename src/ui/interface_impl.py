from .ui_base import interface
from . import dialog_impl
from PySide6 import QtCore, QtGui, QtWidgets
import json
from data.ipa_source_format import IPASourceFormat
import exceptions.ipa_source_exceptions as ipa_source_exceptions


class SourceInterface(interface.Ui_SourceMainWindow, QtWidgets.QMainWindow):
    has_modified = False
    current_file = None

    def __init__(self):
        super().__init__()

    @property
    def app_list(self):
        if not hasattr(self, "_app_list"):
            self._app_list = []
        return self._app_list

    @app_list.setter
    def app_list(self, value: list):
        # Look out for duplicates
        self._app_list = value
        self.update_table()

    def setupUi(self, SourceMainWindow):
        super().setupUi(SourceMainWindow)
        self.actionNew.triggered.connect(self.new_commandLinkButton_onClick)
        self.actionOpen_Database.triggered.connect(self.open_btn_onClick)
        self.actionSave_Database.triggered.connect(self.save_commandLinkButton_onClick)
        self.actionSave_As.triggered.connect(self.save_as_commandLinkButton_onClick)
        self.actionClose.triggered.connect(self.close_file_commandLinkButton_onClick)
        self.actionExit.triggered.connect(SourceMainWindow.close)
        self.Button_Add.clicked.connect(self.add_btn_onClick)
        self.Button_Remove.clicked.connect(self.remove_btn_onClick)
        self.actionAdd_Item.triggered.connect(self.add_btn_onClick)
        self.actionRemove_Item.triggered.connect(self.remove_btn_onClick)
        self.AppsTable.doubleClicked.connect(self.table_double_click)

        # First resize the columns to fit display area, then enable interactive resizing
        self.AppsTable.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Interactive
        )

    def new_commandLinkButton_onClick(self):
        # Make a new blank database
        self.app_list = []
        self.has_modified = True

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
        self.current_file = dialog.selectedFiles()[0]

    def update_table(self):

        # Update the table
        self.AppsTable.setRowCount(len(self.app_list))

        for i, app in enumerate(self.app_list):
            self.AppsTable.setItem(i, 0, QtWidgets.QTableWidgetItem(app.bundleID))
            self.AppsTable.setItem(i, 1, QtWidgets.QTableWidgetItem(app.name))
            self.AppsTable.setItem(i, 2, QtWidgets.QTableWidgetItem(app.version))
            self.AppsTable.setItem(i, 3, QtWidgets.QTableWidgetItem(app.itunesLookup))
            self.AppsTable.setItem(i, 4, QtWidgets.QTableWidgetItem(app.link))

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

        new_item = IPASourceFormat(bundleID, name, version, itunesLookup, link)

        try:
            new_item.validate()
        except ipa_source_exceptions.IPASourceException as e:
            # Show an error message
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.setText("An error occured")
            msg.setInformativeText(e.message)
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()
            return

        self.app_list = self.app_list + [new_item]
        self.has_modified = True

    def remove_btn_onClick(self):
        # If nothing is selected, or list is empty, return
        if self.AppsTable.currentRow() == -1 or not self.app_list:
            return
        # Remove the selected app from the list
        self.app_list.pop(self.AppsTable.currentRow())
        self.update_table()
        self.has_modified = True

    def table_double_click(self, index):
        # Open the edit app dialog
        self.edit_app_dialog = QtWidgets.QDialog()
        self.edit_app_dialog_ui = dialog_impl.EditDialog(
            bundle_id=self.app_list[index.row()].bundleID,
            app_name=self.app_list[index.row()].name,
            version=self.app_list[index.row()].version,
            itunes_lookup=self.app_list[index.row()].itunesLookup,
            download=self.app_list[index.row()].link,
            index=index.row(),
            parent=self,
        )
        self.edit_app_dialog_ui.setupUi(self.edit_app_dialog)
        self.edit_app_dialog.setModal(True)
        self.edit_app_dialog.show()

    def edit_app(self, bundleID, name, version, itunesLookup, link, index):
        # Edit the app
        # print(bundleID, name, version, itunesLookup, link, index)
        new_item = IPASourceFormat(bundleID, name, version, itunesLookup, link)

        try:
            new_item.validate()
        except ipa_source_exceptions.IPASourceException as e:
            # Show an error message
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg.setText("An error occured")
            msg.setInformativeText(e.message)
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()
            return

        self.app_list[index] = new_item
        self.update_table()
        self.has_modified = True

    def save_commandLinkButton_onClick(self):
        # If the user opened a file instead of creating a new one
        if self.current_file:
            # Save the file
            with open(self.current_file, "w") as file:
                json.dump(self.app_list, file, cls=IPASourceFormat.JSONEncoder)
        else:
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
            self.current_file = dialog.selectedFiles()[0]
        self.has_modified = False

    def save_as_commandLinkButton_onClick(self):
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
        self.has_modified = False

    def close_file_commandLinkButton_onClick(self):
        # Close the file
        if self.has_modified:
            # Ask the user if they want to save
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Icon.Question)
            msg.setText("Do you want to save your changes?")
            msg.setStandardButtons(
                QtWidgets.QMessageBox.StandardButton.Yes
                | QtWidgets.QMessageBox.StandardButton.No
                | QtWidgets.QMessageBox.StandardButton.Cancel
            )
            msg.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Yes)
            ret = msg.exec()
            if ret == QtWidgets.QMessageBox.StandardButton.Yes:
                self.save_commandLinkButton_onClick()
            elif ret == QtWidgets.QMessageBox.StandardButton.Cancel:
                return

        self.app_list = []
        self.update_table()
        self.has_modified = False
        self.current_file = None

    def closeEvent(self, event):
        # If the user has modified the file, ask if they want to save
        if self.has_modified:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Icon.Question)
            msg.setText("The file has been modified.")
            msg.setInformativeText("Do you want to save your changes?")
            msg.setStandardButtons(
                QtWidgets.QMessageBox.StandardButton.Save
                | QtWidgets.QMessageBox.StandardButton.Discard
                | QtWidgets.QMessageBox.StandardButton.Cancel
            )
            msg.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Save)
            reply = msg.exec()
            if reply == QtWidgets.QMessageBox.StandardButton.Save:
                self.save_commandLinkButton_onClick()
            elif reply == QtWidgets.QMessageBox.StandardButton.Cancel:
                event.ignore()
                return
        event.accept()

    def exit_commandLinkButton_onClick(self):
        # Close the window
        self.close()
