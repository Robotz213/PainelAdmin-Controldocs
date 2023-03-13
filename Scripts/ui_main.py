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

import rc_icons

class Ui_CrawTo(object):
    def setupUi(self, CrawTo):
        if not CrawTo.objectName():
            CrawTo.setObjectName(u"CrawTo")
        CrawTo.resize(1138, 720)
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
        self.frame_3 = QFrame(self.CadastroUsuario)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 35))
        self.frame_3.setMaximumSize(QSize(16777215, 35))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(397, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.labelCadastro = QLabel(self.frame_3)
        self.labelCadastro.setObjectName(u"labelCadastro")
        font = QFont()
        font.setPointSize(22)
        self.labelCadastro.setFont(font)

        self.horizontalLayout_5.addWidget(self.labelCadastro)

        self.horizontalSpacer_2 = QSpacerItem(396, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.CadastroUsuario)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 545))
        self.frame_4.setStyleSheet(u"background-color: rgba(145, 145, 145, 0.5);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.Nome = QLabel(self.frame_4)
        self.Nome.setObjectName(u"Nome")
        font1 = QFont()
        font1.setPointSize(15)
        self.Nome.setFont(font1)

        self.verticalLayout_6.addWidget(self.Nome)

        self.lineNome = QLineEdit(self.frame_4)
        self.lineNome.setObjectName(u"lineNome")
        self.lineNome.setFont(font1)
        self.lineNome.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_6.addWidget(self.lineNome)


        self.verticalLayout_3.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.CPF = QLabel(self.frame_4)
        self.CPF.setObjectName(u"CPF")
        self.CPF.setFont(font1)

        self.verticalLayout_5.addWidget(self.CPF)

        self.lineCPF = QLineEdit(self.frame_4)
        self.lineCPF.setObjectName(u"lineCPF")
        self.lineCPF.setFont(font1)
        self.lineCPF.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.lineCPF)


        self.verticalLayout_3.addLayout(self.verticalLayout_5)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.Funcao = QLabel(self.frame_4)
        self.Funcao.setObjectName(u"Funcao")
        self.Funcao.setFont(font1)

        self.verticalLayout_7.addWidget(self.Funcao)

        self.lineFuncao = QLineEdit(self.frame_4)
        self.lineFuncao.setObjectName(u"lineFuncao")
        self.lineFuncao.setFont(font1)
        self.lineFuncao.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.lineFuncao)

        self.horizontalSpacer_3 = QSpacerItem(250, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.verticalLayout_7.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.Matricula = QLabel(self.frame_4)
        self.Matricula.setObjectName(u"Matricula")
        self.Matricula.setFont(font1)

        self.verticalLayout_8.addWidget(self.Matricula)

        self.lineMatricula = QLineEdit(self.frame_4)
        self.lineMatricula.setObjectName(u"lineMatricula")
        self.lineMatricula.setFont(font1)
        self.lineMatricula.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.lineMatricula)

        self.horizontalSpacer_4 = QSpacerItem(250, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.verticalLayout_8.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.verticalLayout_8)

        self.SenhaDeAcesso = QLabel(self.frame_4)
        self.SenhaDeAcesso.setObjectName(u"SenhaDeAcesso")
        self.SenhaDeAcesso.setFont(font1)

        self.verticalLayout_3.addWidget(self.SenhaDeAcesso)

        self.lineSenha = QLineEdit(self.frame_4)
        self.lineSenha.setObjectName(u"lineSenha")
        self.lineSenha.setFont(font1)
        self.lineSenha.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.lineSenha)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.InsertemLotes = QPushButton(self.frame_4)
        self.InsertemLotes.setObjectName(u"InsertemLotes")
        self.InsertemLotes.setFont(font1)
        self.InsertemLotes.setCursor(QCursor(Qt.PointingHandCursor))
        self.InsertemLotes.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(132, 132, 132);\n"
"border-radius: 5px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(250, 250, 250);\n"
"border: 2px solid rgb(102, 102, 102);\n"
"border-radius: 5px\n"
"}")

        self.horizontalLayout_6.addWidget(self.InsertemLotes)

        self.Salvar = QPushButton(self.frame_4)
        self.Salvar.setObjectName(u"Salvar")
        self.Salvar.setFont(font1)
        self.Salvar.setCursor(QCursor(Qt.PointingHandCursor))
        self.Salvar.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(132, 132, 132);\n"
"border-radius: 5px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(250, 250, 250);\n"
"border: 2px solid rgb(102, 102, 102);\n"
"border-radius: 5px\n"
"}")

        self.horizontalLayout_6.addWidget(self.Salvar)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_2 = QSpacerItem(20, 212, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.verticalLayout_2.addWidget(self.frame_4)

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
        font2 = QFont()
        font2.setPointSize(12)
        self.CadastrarUsuario.setFont(font2)

        self.horizontalLayout_3.addWidget(self.CadastrarUsuario)

        self.FileUpload = QPushButton(self.frame)
        self.FileUpload.setObjectName(u"FileUpload")
        self.FileUpload.setMinimumSize(QSize(200, 60))
        self.FileUpload.setFont(font2)

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

        self.Pages.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(CrawTo)
    # setupUi

    def retranslateUi(self, CrawTo):
        CrawTo.setWindowTitle(QCoreApplication.translate("CrawTo", u"MainWindow", None))
        self.retornar.setText("")
        self.Sair.setText("")
        self.labelCadastro.setText(QCoreApplication.translate("CrawTo", u"Cadastro de Usu\u00e1rio", None))
        self.Nome.setText(QCoreApplication.translate("CrawTo", u"NOME COMPLETO", None))
        self.CPF.setText(QCoreApplication.translate("CrawTo", u"CPF", None))
        self.Funcao.setText(QCoreApplication.translate("CrawTo", u"E-mail", None))
        self.Matricula.setText(QCoreApplication.translate("CrawTo", u"MATRICULA", None))
        self.SenhaDeAcesso.setText(QCoreApplication.translate("CrawTo", u"SENHA DE ACESSO", None))
        self.InsertemLotes.setText(QCoreApplication.translate("CrawTo", u"Cadastro em Lotes", None))
        self.Salvar.setText(QCoreApplication.translate("CrawTo", u"Salvar Altera\u00e7\u00f5es", None))
        self.CadastrarUsuario.setText(QCoreApplication.translate("CrawTo", u"Cadastrar Usu\u00e1rio", None))
        self.FileUpload.setText(QCoreApplication.translate("CrawTo", u"Upload de Arquivos", None))
    # retranslateUi

