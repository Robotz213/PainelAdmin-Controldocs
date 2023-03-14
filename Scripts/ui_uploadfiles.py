# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uploadfiles.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Cadastro(object):
    def setupUi(self, Cadastro):
        if not Cadastro.objectName():
            Cadastro.setObjectName(u"Cadastro")
        Cadastro.resize(370, 144)
        Cadastro.setMinimumSize(QSize(370, 120))
        Cadastro.setMaximumSize(QSize(370, 144))
        Cadastro.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayout_4 = QVBoxLayout(Cadastro)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget = QWidget(Cadastro)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(140, 140, 140);")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 0.3);")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 2px;\n"
"")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.BuscarPlanilha = QPushButton(self.frame)
        self.BuscarPlanilha.setObjectName(u"BuscarPlanilha")
        self.BuscarPlanilha.setFont(font)
        self.BuscarPlanilha.setCursor(QCursor(Qt.PointingHandCursor))
        self.BuscarPlanilha.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(255, 255, 255, 0.5);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(102, 102, 102);\n"
"border-radius: 5px\n"
"}")

        self.horizontalLayout.addWidget(self.BuscarPlanilha)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addWidget(self.frame)

        self.IniciarUpload = QPushButton(self.widget)
        self.IniciarUpload.setObjectName(u"IniciarUpload")
        self.IniciarUpload.setFont(font)
        self.IniciarUpload.setCursor(QCursor(Qt.PointingHandCursor))
        self.IniciarUpload.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(255, 255, 255, 0.5);\n"
"border: 3px solid rgb(132, 132, 132);\n"
"border-radius: 5px;\n"
"margin: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(102, 102, 102);\n"
"border-radius: 5px\n"
"}")

        self.verticalLayout_3.addWidget(self.IniciarUpload)


        self.verticalLayout_4.addWidget(self.widget, 0, Qt.AlignVCenter)


        self.retranslateUi(Cadastro)

        QMetaObject.connectSlotsByName(Cadastro)
    # setupUi

    def retranslateUi(self, Cadastro):
        Cadastro.setWindowTitle(QCoreApplication.translate("Cadastro", u"Form", None))
        self.label.setText(QCoreApplication.translate("Cadastro", u"Informe a planilha com arquivos a serem enviados", None))
        self.BuscarPlanilha.setText(QCoreApplication.translate("Cadastro", u"Buscar", None))
        self.IniciarUpload.setText(QCoreApplication.translate("Cadastro", u"Iniciar", None))
    # retranslateUi

