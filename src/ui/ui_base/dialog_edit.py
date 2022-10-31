# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_edit.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QGridLayout, QLabel, QLineEdit,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_AddSourceDialog(object):
    def setupUi(self, AddSourceDialog):
        if not AddSourceDialog.objectName():
            AddSourceDialog.setObjectName(u"AddSourceDialog")
        AddSourceDialog.setWindowModality(Qt.ApplicationModal)
        AddSourceDialog.resize(400, 221)
        self.gridLayout = QGridLayout(AddSourceDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(AddSourceDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignCenter)
        self.download_label = QLabel(AddSourceDialog)
        self.download_label.setObjectName(u"download_label")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.download_label)

        self.itunes_label = QLabel(AddSourceDialog)
        self.itunes_label.setObjectName(u"itunes_label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.itunes_label)

        self.version_label = QLabel(AddSourceDialog)
        self.version_label.setObjectName(u"version_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.version_label)

        self.appname_label = QLabel(AddSourceDialog)
        self.appname_label.setObjectName(u"appname_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.appname_label)

        self.bundleid_edit = QLineEdit(AddSourceDialog)
        self.bundleid_edit.setObjectName(u"bundleid_edit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.bundleid_edit)

        self.appname_edit = QLineEdit(AddSourceDialog)
        self.appname_edit.setObjectName(u"appname_edit")
        self.appname_edit.setClearButtonEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.appname_edit)

        self.version_edit = QLineEdit(AddSourceDialog)
        self.version_edit.setObjectName(u"version_edit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.version_edit)

        self.itunes_edit = QLineEdit(AddSourceDialog)
        self.itunes_edit.setObjectName(u"itunes_edit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.itunes_edit)

        self.download_edit = QLineEdit(AddSourceDialog)
        self.download_edit.setObjectName(u"download_edit")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.download_edit)

        self.bundleid_label = QLabel(AddSourceDialog)
        self.bundleid_label.setObjectName(u"bundleid_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.bundleid_label)


        self.verticalLayout.addLayout(self.formLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(AddSourceDialog)
        self.buttonBox.accepted.connect(AddSourceDialog.accept)
        self.buttonBox.rejected.connect(AddSourceDialog.reject)

        QMetaObject.connectSlotsByName(AddSourceDialog)
    # setupUi

    def retranslateUi(self, AddSourceDialog):
        AddSourceDialog.setWindowTitle(QCoreApplication.translate("AddSourceDialog", u"Add Source", None))
        self.download_label.setText(QCoreApplication.translate("AddSourceDialog", u"Download Link", None))
        self.itunes_label.setText(QCoreApplication.translate("AddSourceDialog", u"iTunes Link", None))
        self.version_label.setText(QCoreApplication.translate("AddSourceDialog", u"App Version", None))
        self.appname_label.setText(QCoreApplication.translate("AddSourceDialog", u"Bundle ID", None))
        self.bundleid_label.setText(QCoreApplication.translate("AddSourceDialog", u"App Name", None))
    # retranslateUi

