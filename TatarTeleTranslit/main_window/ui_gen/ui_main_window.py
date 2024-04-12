# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1002, 736)
        MainWindow.setLocale(QLocale(QLocale.Tatar, QLocale.Russia))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.source_label = QLabel(self.centralwidget)
        self.source_label.setObjectName(u"source_label")

        self.horizontalLayout.addWidget(self.source_label)

        self.source_combobox = QComboBox(self.centralwidget)
        self.source_combobox.setObjectName(u"source_combobox")
        self.source_combobox.setLocale(QLocale(QLocale.Tatar, QLocale.Russia))

        self.horizontalLayout.addWidget(self.source_combobox)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalSpacer_3 = QSpacerItem(238, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.target_label = QLabel(self.centralwidget)
        self.target_label.setObjectName(u"target_label")

        self.horizontalLayout_3.addWidget(self.target_label)

        self.target_combobox = QComboBox(self.centralwidget)
        self.target_combobox.setObjectName(u"target_combobox")
        self.target_combobox.setLocale(QLocale(QLocale.Tatar, QLocale.Russia))

        self.horizontalLayout_3.addWidget(self.target_combobox)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.source_textedit = QTextEdit(self.centralwidget)
        self.source_textedit.setObjectName(u"source_textedit")

        self.verticalLayout.addWidget(self.source_textedit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.translit_button = QPushButton(self.centralwidget)
        self.translit_button.setObjectName(u"translit_button")

        self.horizontalLayout_2.addWidget(self.translit_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.target_textedit = QTextEdit(self.centralwidget)
        self.target_textedit.setObjectName(u"target_textedit")
        self.target_textedit.setReadOnly(True)

        self.verticalLayout.addWidget(self.target_textedit)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.source_label.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0448\u043b\u0430\u043d\u0433\u044b\u0447", None))
        self.target_label.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u043a\u0441\u0430\u0442\u043b\u044b", None))
        self.translit_button.setText(QCoreApplication.translate("MainWindow", u"Translit", None))
    # retranslateUi

