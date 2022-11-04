from .ui_base import dialog_edit
from PySide6 import QtCore, QtGui, QtWidgets
import re
import urllib
import urllib.error, urllib.request
import json


class NewDialog(dialog_edit.Ui_AddSourceDialog, QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

    def setupUi(self, AddSourceDialog):
        super().setupUi(AddSourceDialog)
        self.buttonBox.accepted.connect(self.add_btn_onClick)
        self.query_btn.clicked.connect(self.query_server_for_app)

    def add_btn_onClick(self):
        self.parent.add_app(
            self.bundleid_edit.text(),
            self.appname_edit.text(),
            self.version_edit.text(),
            self.itunes_edit.text(),
            self.download_edit.text(),
        )
        self.close()

    def query_server_for_app(self):
        # Lookup URL: https://itunes.apple.com/lookup?bundleId=net.angelxwind.appsyncunified or https://itunes.apple.com/lookup?id=284882215
        # App URL: https://itunes.apple.com/us/app/appsync-unified/id1107421413?mt=8 or https://apps.apple.com/us/app/appsync-unified/id1107421413?mt=8
        lookup_url = ""

        itunes_clue = self.itunes_edit.text()
        bundleid_clue = self.bundleid_edit.text()

        if itunes_clue.startswith(
            "https://itunes.apple.com/"
        ) or itunes_clue.startswith("https://apps.apple.com/"):
            if "lookup?" in self.itunes_edit.text():
                lookup_url = self.itunes_edit.text()
                pass
            elif re.search(r"id=?\d+", self.itunes_edit.text()):
                # This is an app ID
                appID = re.search(r"(?<=id)(=?)(\d+)", self.itunes_edit.text()).group(2)
                lookup_url = f"https://itunes.apple.com/lookup?id={appID}"
                pass
        elif bundleid_clue != "":
            # This is a bundle
            lookup_url = (
                f"https://itunes.apple.com/lookup?bundleId={self.bundleid_edit.text()}"
            )
            pass
        else:
            # No info to go off of. Bail
            warning = QtWidgets.QMessageBox()
            warning.setText("Error")
            warning.setInformativeText(
                "No information to query the App Store with. Please enter an App Store URL or a bundle ID."
            )
            warning.setModal(True)
            warning.exec()

            return

        # Query the server
        try:
            response = urllib.request.urlopen(lookup_url)
            data = json.loads(response.read())
        except urllib.error.HTTPError as e:
            warning = QtWidgets.QMessageBox()
            warning.setText("Error")
            warning.setInformativeText(
                f"An error occured while querying the App Store. Error code: {e.code}"
            )
            warning.setModal(True)
            warning.exec()

            return

        # Check if the app was found
        if data["resultCount"] == 0:
            warning = QtWidgets.QMessageBox()
            warning.setText("Error")
            warning.setInformativeText(
                "The App Store could not find an app with the information provided."
            )
            warning.setModal(True)
            warning.exec()

            return

        # Set the app name
        self.appname_edit.setText(data["results"][0]["trackName"])
        self.version_edit.setText(data["results"][0]["version"])
        self.bundleid_edit.setText(data["results"][0]["bundleId"])
        self.itunes_edit.setText(
            f"https://itunes.apple.com/lookup?bundleId={data['results'][0]['bundleId']}"
        )


class EditDialog(NewDialog):
    def __init__(
        self, bundle_id, app_name, version, itunes_lookup, download, index, parent=None
    ):
        super().__init__(parent=parent)
        self.parent = parent
        self.bundle_id = bundle_id
        self.app_name = app_name
        self.version = version
        self.itunes_lookup = itunes_lookup
        self.download = download
        self.index = index

    def setupUi(self, AddSourceDialog):
        super().setupUi(AddSourceDialog)
        self.bundleid_edit.setText(self.bundle_id)
        self.appname_edit.setText(self.app_name)
        self.version_edit.setText(self.version)
        self.itunes_edit.setText(self.itunes_lookup)
        self.download_edit.setText(self.download)
        self.windowTitle = "Edit App"

    def add_btn_onClick(self):
        self.parent.edit_app(
            self.bundleid_edit.text(),
            self.appname_edit.text(),
            self.version_edit.text(),
            self.itunes_edit.text(),
            self.download_edit.text(),
            self.index,
        )
        self.close()
