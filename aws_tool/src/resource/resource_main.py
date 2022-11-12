# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'resource_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(954, 569)
        font = QFont()
        font.setFamily(u"Times New Roman")
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(24)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 6)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 934, 467))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_tableWidget = QTableWidget(self.scrollAreaWidgetContents)
        if (self.main_tableWidget.columnCount() < 4):
            self.main_tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.main_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.main_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.main_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.main_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.main_tableWidget.setObjectName(u"main_tableWidget")
        self.main_tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.main_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout.addWidget(self.main_tableWidget, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 1, 6)

        self.refresh_pushButton = QPushButton(self.centralwidget)
        self.refresh_pushButton.setObjectName(u"refresh_pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refresh_pushButton.sizePolicy().hasHeightForWidth())
        self.refresh_pushButton.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamily(u"Times New Roman")
        font2.setPointSize(16)
        font2.setKerning(True)
        self.refresh_pushButton.setFont(font2)

        self.gridLayout_2.addWidget(self.refresh_pushButton, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 2, 2, 1, 1)

        self.start_pushButton = QPushButton(self.centralwidget)
        self.start_pushButton.setObjectName(u"start_pushButton")
        sizePolicy.setHeightForWidth(self.start_pushButton.sizePolicy().hasHeightForWidth())
        self.start_pushButton.setSizePolicy(sizePolicy)
        self.start_pushButton.setMinimumSize(QSize(4, 0))
        font3 = QFont()
        font3.setFamily(u"Times New Roman")
        font3.setPointSize(16)
        self.start_pushButton.setFont(font3)

        self.gridLayout_2.addWidget(self.start_pushButton, 2, 3, 1, 1)

        self.stop_pushButton = QPushButton(self.centralwidget)
        self.stop_pushButton.setObjectName(u"stop_pushButton")
        sizePolicy.setHeightForWidth(self.stop_pushButton.sizePolicy().hasHeightForWidth())
        self.stop_pushButton.setSizePolicy(sizePolicy)
        self.stop_pushButton.setFont(font3)

        self.gridLayout_2.addWidget(self.stop_pushButton, 2, 4, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"AWS Instances", None))
        ___qtablewidgetitem = self.main_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Instance", None));
        ___qtablewidgetitem1 = self.main_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.main_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"PublicIpAddress", None));
        ___qtablewidgetitem3 = self.main_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"InstanceState", None));
        self.refresh_pushButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.start_pushButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.stop_pushButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
    # retranslateUi

