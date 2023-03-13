# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastroemlotes.ui'
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
        Cadastro.resize(332, 352)
        Cadastro.setMinimumSize(QSize(332, 352))
        Cadastro.setMaximumSize(QSize(332, 352))
        self.verticalLayout_4 = QVBoxLayout(Cadastro)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(Cadastro)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(15)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setTextFormat(Qt.PlainText)
        self.label.setWordWrap(True)
        self.label.setMargin(5)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        font1 = QFont()
        font1.setPointSize(21)
        self.lineEdit.setFont(font1)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        font2 = QFont()
        font2.setPointSize(15)
        font2.setKerning(False)
        self.pushButton.setFont(font2)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font2)

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)


        self.verticalLayout_4.addWidget(self.frame)


        self.retranslateUi(Cadastro)

        QMetaObject.connectSlotsByName(Cadastro)
    # setupUi

    def retranslateUi(self, Cadastro):
        Cadastro.setWindowTitle(QCoreApplication.translate("Cadastro", u"Form", None))
        self.label.setText(QCoreApplication.translate("Cadastro", u"Informe a Planilha com os Usu\u00e1rios para cadastro no sistema", None))
        self.pushButton_2.setText(QCoreApplication.translate("Cadastro", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("Cadastro", u"Planilha Exemplo", None))
        self.pushButton_3.setText(QCoreApplication.translate("Cadastro", u"Iniciar", None))
    # retranslateUi

