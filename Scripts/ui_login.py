# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 600)
        Form.setMinimumSize(QSize(400, 600))
        Form.setMaximumSize(QSize(400, 600))
        Form.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 40))
        self.frame.setStyleSheet(u"background-color: rgb(58,58,58);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(58,58,58);")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(500, 16777215))
        self.frame_4.setStyleSheet(u"background-color: rgb(58,58,58);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.UserFrame = QLineEdit(self.frame_4)
        self.UserFrame.setObjectName(u"UserFrame")
        self.UserFrame.setGeometry(QRect(41, 264, 300, 50))
        self.UserFrame.setMinimumSize(QSize(300, 50))
        self.UserFrame.setMaximumSize(QSize(300, 30))
        font = QFont()
        font.setPointSize(12)
        self.UserFrame.setFont(font)
        self.UserFrame.setAutoFillBackground(False)
        self.UserFrame.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(45,45,45);\n"
"	border-radius: 5px;\n"
"	padding: 15px;\n"
"	background-color: rgb(131, 131, 131);\n"
"	\n"
"}")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(191, 29, 16, 200))
        self.frame_5.setMaximumSize(QSize(200, 200))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.PasswordFrame = QLineEdit(self.frame_4)
        self.PasswordFrame.setObjectName(u"PasswordFrame")
        self.PasswordFrame.setGeometry(QRect(41, 329, 300, 50))
        self.PasswordFrame.setMinimumSize(QSize(300, 50))
        self.PasswordFrame.setMaximumSize(QSize(300, 30))
        self.PasswordFrame.setFont(font)
        self.PasswordFrame.setCursor(QCursor(Qt.IBeamCursor))
        self.PasswordFrame.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(45,45,45);\n"
"	border-radius: 5px;\n"
"	padding: 15px;\n"
"	background-color: rgb(131, 131, 131);\n"
"	\n"
"}")
        self.PasswordFrame.setInputMask(u"")
        self.PasswordFrame.setEchoMode(QLineEdit.Password)
        self.EnterButton = QPushButton(self.frame_4)
        self.EnterButton.setObjectName(u"EnterButton")
        self.EnterButton.setGeometry(QRect(51, 411, 281, 30))
        self.EnterButton.setMinimumSize(QSize(200, 30))
        self.EnterButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.EnterButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(93, 93, 93);\n"
"border: 2px solid rgb(132, 132, 132);\n"
"border-radius: 5px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(73, 73, 73);\n"
"border: 2px solid rgb(102, 102, 102);\n"
"border-radius: 5px\n"
"}")

        self.horizontalLayout.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 40))
        self.frame_3.setStyleSheet(u"background-color: rgb(58,58,58);")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.UserFrame.setInputMask("")
        self.UserFrame.setText("")
        self.UserFrame.setPlaceholderText(QCoreApplication.translate("Form", u"Usu\u00e1rio", None))
        self.PasswordFrame.setText("")
        self.PasswordFrame.setPlaceholderText(QCoreApplication.translate("Form", u"Senha", None))
        self.EnterButton.setText(QCoreApplication.translate("Form", u"Entrar", None))
    # retranslateUi

