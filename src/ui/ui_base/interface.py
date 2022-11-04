# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHeaderView,
    QLayout, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_SourceMainWindow(object):
    def setupUi(self, SourceMainWindow):
        if not SourceMainWindow.objectName():
            SourceMainWindow.setObjectName(u"SourceMainWindow")
        SourceMainWindow.resize(800, 600)
        self.actionOpen_Database = QAction(SourceMainWindow)
        self.actionOpen_Database.setObjectName(u"actionOpen_Database")
        self.actionSave_Database = QAction(SourceMainWindow)
        self.actionSave_Database.setObjectName(u"actionSave_Database")
        self.actionExit = QAction(SourceMainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAdd_Item = QAction(SourceMainWindow)
        self.actionAdd_Item.setObjectName(u"actionAdd_Item")
        self.actionRemove_Item = QAction(SourceMainWindow)
        self.actionRemove_Item.setObjectName(u"actionRemove_Item")
        self.actionNew = QAction(SourceMainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionSave_As = QAction(SourceMainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.centralwidget = QWidget(SourceMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.Button_Add = QPushButton(self.centralwidget)
        self.Button_Add.setObjectName(u"Button_Add")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Button_Add.sizePolicy().hasHeightForWidth())
        self.Button_Add.setSizePolicy(sizePolicy1)
        self.Button_Add.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout.addWidget(self.Button_Add)

        self.Button_Remove = QPushButton(self.centralwidget)
        self.Button_Remove.setObjectName(u"Button_Remove")

        self.verticalLayout.addWidget(self.Button_Remove)


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.AppsTable = QTableWidget(self.centralwidget)
        if (self.AppsTable.columnCount() < 5):
            self.AppsTable.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.AppsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.AppsTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.AppsTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.AppsTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.AppsTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.AppsTable.setObjectName(u"AppsTable")
        self.AppsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.AppsTable.setAlternatingRowColors(True)
        self.AppsTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.AppsTable.setSortingEnabled(False)

        self.gridLayout.addWidget(self.AppsTable, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        SourceMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SourceMainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        SourceMainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SourceMainWindow)
        self.statusbar.setObjectName(u"statusbar")
        SourceMainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen_Database)
        self.menuFile.addAction(self.actionSave_Database)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionAdd_Item)
        self.menuEdit.addAction(self.actionRemove_Item)

        self.retranslateUi(SourceMainWindow)

        QMetaObject.connectSlotsByName(SourceMainWindow)
    # setupUi

    def retranslateUi(self, SourceMainWindow):
        SourceMainWindow.setWindowTitle(QCoreApplication.translate("SourceMainWindow", u"IPA Source Editor (Alpha)", None))
        self.actionOpen_Database.setText(QCoreApplication.translate("SourceMainWindow", u"Open...", None))
#if QT_CONFIG(shortcut)
        self.actionOpen_Database.setShortcut(QCoreApplication.translate("SourceMainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_Database.setText(QCoreApplication.translate("SourceMainWindow", u"Save...", None))
#if QT_CONFIG(shortcut)
        self.actionSave_Database.setShortcut(QCoreApplication.translate("SourceMainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("SourceMainWindow", u"Exit", None))
        self.actionAdd_Item.setText(QCoreApplication.translate("SourceMainWindow", u"Add Item", None))
#if QT_CONFIG(shortcut)
        self.actionAdd_Item.setShortcut(QCoreApplication.translate("SourceMainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionRemove_Item.setText(QCoreApplication.translate("SourceMainWindow", u"Remove Item", None))
#if QT_CONFIG(shortcut)
        self.actionRemove_Item.setShortcut(QCoreApplication.translate("SourceMainWindow", u"Ctrl+Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.actionNew.setText(QCoreApplication.translate("SourceMainWindow", u"New...", None))
        self.actionSave_As.setText(QCoreApplication.translate("SourceMainWindow", u"Save As...", None))
        self.Button_Add.setText(QCoreApplication.translate("SourceMainWindow", u"Add", None))
        self.Button_Remove.setText(QCoreApplication.translate("SourceMainWindow", u"Remove", None))
        ___qtablewidgetitem = self.AppsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("SourceMainWindow", u"Bundle ID", None));
        ___qtablewidgetitem1 = self.AppsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("SourceMainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.AppsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("SourceMainWindow", u"Version", None));
        ___qtablewidgetitem3 = self.AppsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("SourceMainWindow", u"iTunes Link", None));
        ___qtablewidgetitem4 = self.AppsTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("SourceMainWindow", u"Download Link", None));
        self.menuFile.setTitle(QCoreApplication.translate("SourceMainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("SourceMainWindow", u"Edit", None))
    # retranslateUi

