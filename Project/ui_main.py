# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_CrawTo(object):
    def setupUi(self, CrawTo):
        if not CrawTo.objectName():
            CrawTo.setObjectName(u"CrawTo")
        CrawTo.resize(1138, 727)
        CrawTo.setStyleSheet(u"")
        self.centralwidget = QWidget(CrawTo)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1138, 720))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Dockbar = QFrame(self.centralwidget)
        self.Dockbar.setObjectName(u"Dockbar")
        self.Dockbar.setMinimumSize(QSize(64, 480))
        self.Dockbar.setMaximumSize(QSize(60, 16777215))
        self.Dockbar.setStyleSheet(u"background-color: rgb(0, 0, 127);\n"
"")
        self.Dockbar.setFrameShape(QFrame.NoFrame)
        self.Dockbar.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.Dockbar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.retornar = QPushButton(self.Dockbar)
        self.retornar.setObjectName(u"retornar")
        self.retornar.setMinimumSize(QSize(48, 50))
        self.retornar.setMaximumSize(QSize(45, 50))
        self.retornar.setStyleSheet(u"QPushButton{\n"
"image: url(:/home/Icons/retorna.png);\n"
"background-color: rgba(255, 255, 255, 0.5);\n"
"border: 2px solid rgb(132, 132, 132);\n"
"border-radius: 5px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(102, 102, 102);\n"
"border-radius: 5px\n"
"}")

        self.verticalLayout.addWidget(self.retornar)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.Sair = QPushButton(self.Dockbar)
        self.Sair.setObjectName(u"Sair")
        self.Sair.setMinimumSize(QSize(48, 50))
        self.Sair.setMaximumSize(QSize(45, 50))
        self.Sair.setCursor(QCursor(Qt.PointingHandCursor))
        self.Sair.setStyleSheet(u"QPushButton{\n"
"image: url(:/home/Icons/sair.png);\n"
"background-color: rgba(255, 255, 255, 0.5);\n"
"border: 2px solid rgb(132, 132, 132);\n"
"border-radius: 5px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(102, 102, 102);\n"
"border-radius: 5px\n"
"}")

        self.verticalLayout.addWidget(self.Sair)


        self.horizontalLayout.addWidget(self.Dockbar)

        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        self.CadastroUsuario = QWidget()
        self.CadastroUsuario.setObjectName(u"CadastroUsuario")
        self.verticalLayout_2 = QVBoxLayout(self.CadastroUsuario)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.CadastroUsuario)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignHCenter)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.CadastroUsuario)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(15)
        self.label_2.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.CadastroUsuario)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font1)

        self.horizontalLayout_5.addWidget(self.lineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.CadastroUsuario)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(self.CadastroUsuario)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font1)

        self.horizontalLayout_6.addWidget(self.lineEdit_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.CadastroUsuario)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_4)

        self.lineEdit_3 = QLineEdit(self.CadastroUsuario)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFont(font1)

        self.horizontalLayout_7.addWidget(self.lineEdit_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_5 = QLabel(self.CadastroUsuario)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label_5)

        self.lineEdit_4 = QLineEdit(self.CadastroUsuario)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setFont(font1)

        self.horizontalLayout_8.addWidget(self.lineEdit_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.pushButton = QPushButton(self.CadastroUsuario)
        self.pushButton.setObjectName(u"pushButton")
        font2 = QFont()
        font2.setPointSize(22)
        self.pushButton.setFont(font2)

        self.verticalLayout_2.addWidget(self.pushButton)

        self.Pages.addWidget(self.CadastroUsuario)
        self.UploadArquivos = QWidget()
        self.UploadArquivos.setObjectName(u"UploadArquivos")
        self.Pages.addWidget(self.UploadArquivos)
        self.MenuPrincipal = QWidget()
        self.MenuPrincipal.setObjectName(u"MenuPrincipal")
        self.horizontalLayout_2 = QHBoxLayout(self.MenuPrincipal)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.MenuPrincipal)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setIconSize(QSize(0, 0))
        self.tabWidget.setUsesScrollButtons(False)
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(200, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.CadastrarUsuario = QPushButton(self.frame)
        self.CadastrarUsuario.setObjectName(u"CadastrarUsuario")
        self.CadastrarUsuario.setMinimumSize(QSize(200, 60))
        font3 = QFont()
        font3.setPointSize(12)
        self.CadastrarUsuario.setFont(font3)

        self.horizontalLayout_3.addWidget(self.CadastrarUsuario)

        self.FileUpload = QPushButton(self.frame)
        self.FileUpload.setObjectName(u"FileUpload")
        self.FileUpload.setMinimumSize(QSize(200, 60))
        self.FileUpload.setFont(font3)

        self.horizontalLayout_3.addWidget(self.FileUpload)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.tabWidget.addTab(self.widget, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), u"")

        self.horizontalLayout_2.addWidget(self.tabWidget)

        self.Pages.addWidget(self.MenuPrincipal)

        self.horizontalLayout.addWidget(self.Pages)

        CrawTo.setCentralWidget(self.centralwidget)

        self.retranslateUi(CrawTo)

        self.Pages.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(CrawTo)
    # setupUi

    def retranslateUi(self, CrawTo):
        CrawTo.setWindowTitle(QCoreApplication.translate("CrawTo", u"MainWindow", None))
        self.retornar.setText("")
        self.Sair.setText("")
        self.label.setText(QCoreApplication.translate("CrawTo", u"Cadastro de Usu\u00e1rio", None))
        self.label_2.setText(QCoreApplication.translate("CrawTo", u"Nome", None))
        self.label_3.setText(QCoreApplication.translate("CrawTo", u"Sobrenome", None))
        self.label_4.setText(QCoreApplication.translate("CrawTo", u"Senha", None))
        self.label_5.setText(QCoreApplication.translate("CrawTo", u"E-mail", None))
        self.pushButton.setText(QCoreApplication.translate("CrawTo", u"SALVAR", None))
        self.CadastrarUsuario.setText(QCoreApplication.translate("CrawTo", u"Cadastrar Usu\u00e1rio", None))
        self.FileUpload.setText(QCoreApplication.translate("CrawTo", u"Upload de Arquivos", None))
    # retranslateUi

