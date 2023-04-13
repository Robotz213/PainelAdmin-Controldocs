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
        CrawTo.resize(1138, 720)
        CrawTo.setMinimumSize(QSize(1, 60))
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
        self.Dockbar.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"")
        self.Dockbar.setFrameShape(QFrame.NoFrame)
        self.Dockbar.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.Dockbar)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.retornar = QPushButton(self.Dockbar)
        self.retornar.setObjectName(u"retornar")
        self.retornar.setMinimumSize(QSize(48, 50))
        self.retornar.setMaximumSize(QSize(45, 50))
        self.retornar.setCursor(QCursor(Qt.PointingHandCursor))
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
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.CadastroUsuario)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QSize(0, 50))
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_3)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer = QSpacerItem(397, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)

        self.labelCadastro = QLabel(self.frame_3)
        self.labelCadastro.setObjectName(u"labelCadastro")
        font = QFont()
        font.setPointSize(22)
        self.labelCadastro.setFont(font)
        self.labelCadastro.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.labelCadastro)

        self.horizontalSpacer_2 = QSpacerItem(396, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)


        self.verticalLayout_18.addLayout(self.horizontalLayout_9)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.CadastroUsuario)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 545))
        self.frame_4.setStyleSheet(u"background-color: rgba(145, 145, 145, 0.5);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_4)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(20, 37, 59, 0.4);")
        self.verticalLayout_16 = QVBoxLayout(self.frame)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalSpacer_7 = QSpacerItem(20, 90, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_4.addItem(self.verticalSpacer_5)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_4)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.Nome = QLabel(self.frame)
        self.Nome.setObjectName(u"Nome")
        font1 = QFont()
        font1.setPointSize(15)
        self.Nome.setFont(font1)
        self.Nome.setStyleSheet(u"QLabel{\n"
"	background-color: rgba(255, 255, 255, 0.5);\n"
"  	border: 2px solid rgb(132, 132, 132);\n"
"  	border-radius: 5px;\n"
"	padding: 2px;\n"
"}")

        self.verticalLayout_6.addWidget(self.Nome)

        self.lineNome = QLineEdit(self.frame)
        self.lineNome.setObjectName(u"lineNome")
        self.lineNome.setFont(font1)
        self.lineNome.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"  	border: 2px solid rgb(132, 132, 132);\n"
"  	border-radius: 5px;\n"
"\n"
"}\n"
"")

        self.verticalLayout_6.addWidget(self.lineNome)


        self.verticalLayout_15.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.CPF = QLabel(self.frame)
        self.CPF.setObjectName(u"CPF")
        self.CPF.setFont(font1)
        self.CPF.setStyleSheet(u"QLabel{\n"
"	background-color: rgba(255, 255, 255, 0.5);\n"
"  	border: 2px solid rgb(132, 132, 132);\n"
"  	border-radius: 5px;\n"
"	padding: 2px;\n"
"}")

        self.verticalLayout_5.addWidget(self.CPF)

        self.lineCPF = QLineEdit(self.frame)
        self.lineCPF.setObjectName(u"lineCPF")
        self.lineCPF.setFont(font1)
        self.lineCPF.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"  	border: 2px solid rgb(132, 132, 132);\n"
"  	border-radius: 5px;\n"
"\n"
"}\n"
"")

        self.verticalLayout_5.addWidget(self.lineCPF)


        self.verticalLayout_15.addLayout(self.verticalLayout_5)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.Funcao = QLabel(self.frame)
        self.Funcao.setObjectName(u"Funcao")
        self.Funcao.setFont(font1)
        self.Funcao.setStyleSheet(u"QLabel{\n"
"	background-color: rgba(255, 255, 255, 0.5);\n"
"  	border: 2px solid rgb(132, 132, 132);\n"
"  	border-radius: 5px;\n"
"	padding: 2px;\n"
"}")

        self.verticalLayout_7.addWidget(self.Funcao)

        self.lineMails = QLineEdit(self.frame)
        self.lineMails.setObjectName(u"lineMails")
        self.lineMails.setFont(font1)
        self.lineMails.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"  	border: 2px solid rgb(132, 132, 132);\n"
"  	border-radius: 5px;\n"
"\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.lineMails)

        self.horizontalSpacer_3 = QSpacerItem(250, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.verticalLayout_7.addItem(self.horizontalSpacer_3)


        self.verticalLayout_15.addLayout(self.verticalLayout_7)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setStyleSheet(u"QLabel{\n"
"	background-color: rgba(255, 255, 255, 0.5);\n"
"  	border: 2px solid rgb(132, 132, 132);\n"
"  	border-radius: 5px;\n"
"	padding: 2px;\n"
"}")

        self.verticalLayout_3.addWidget(self.label)

        self.UsuarioTipo = QComboBox(self.frame)
        self.UsuarioTipo.addItem("")
        self.UsuarioTipo.addItem("")
        self.UsuarioTipo.addItem("")
        self.UsuarioTipo.setObjectName(u"UsuarioTipo")
        font2 = QFont()
        font2.setPointSize(12)
        self.UsuarioTipo.setFont(font2)
        self.UsuarioTipo.setStyleSheet(u"QComboBox{\n"
"	\n"
"	\n"
"	background-color: rgb(200, 200, 200);\n"
"  	border: 2px solid rgb(132, 132, 132);\n"
"  	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"\n"
"QComboBox:pressed {\n"
"  background-color: rgb(200, 200, 200);\n"
"  border: 3px solid rgb(102, 102, 102);\n"
"  border-radius: 5px;\n"
"}\n"
"\n"
"")

        self.verticalLayout_3.addWidget(self.UsuarioTipo)


        self.verticalLayout_15.addLayout(self.verticalLayout_3)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")

        self.verticalLayout_14.addLayout(self.verticalLayout_9)

        self.horizontalSpacer_4 = QSpacerItem(250, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.verticalLayout_14.addItem(self.horizontalSpacer_4)


        self.verticalLayout_15.addLayout(self.verticalLayout_14)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.SenhaDeAcesso = QLabel(self.frame)
        self.SenhaDeAcesso.setObjectName(u"SenhaDeAcesso")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.SenhaDeAcesso.sizePolicy().hasHeightForWidth())
        self.SenhaDeAcesso.setSizePolicy(sizePolicy1)
        self.SenhaDeAcesso.setFont(font1)
        self.SenhaDeAcesso.setStyleSheet(u"QLabel{\n"
"	background-color: rgba(255, 255, 255, 0.5);\n"
"  	border: 2px solid rgb(132, 132, 132);\n"
"  	border-radius: 5px;\n"
"	padding: 2px;\n"
"}")

        self.verticalLayout_8.addWidget(self.SenhaDeAcesso)

        self.lineSenha = QLineEdit(self.frame)
        self.lineSenha.setObjectName(u"lineSenha")
        self.lineSenha.setMinimumSize(QSize(183, 0))
        self.lineSenha.setMaximumSize(QSize(183, 16777215))
        self.lineSenha.setFont(font1)
        self.lineSenha.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"  	border: 2px solid rgb(132, 132, 132);\n"
"  	border-radius: 5px;\n"
"\n"
"}\n"
"")

        self.verticalLayout_8.addWidget(self.lineSenha)


        self.horizontalLayout_7.addLayout(self.verticalLayout_8)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"QLabel{\n"
"	background-color: rgba(255, 255, 255, 0.5);\n"
"  	border: 2px solid rgb(132, 132, 132);\n"
"  	border-radius: 5px;\n"
"	padding: 2px;\n"
"}")

        self.verticalLayout_4.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(183, 0))
        self.lineEdit_2.setMaximumSize(QSize(183, 16777215))
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"  	border: 2px solid rgb(132, 132, 132);\n"
"  	border-radius: 5px;\n"
"\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.lineEdit_2)


        self.horizontalLayout_7.addLayout(self.verticalLayout_4)


        self.verticalLayout_15.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.InsertemLotes = QPushButton(self.frame)
        self.InsertemLotes.setObjectName(u"InsertemLotes")
        self.InsertemLotes.setMinimumSize(QSize(0, 50))
        self.InsertemLotes.setFont(font1)
        self.InsertemLotes.setCursor(QCursor(Qt.PointingHandCursor))
        self.InsertemLotes.setStyleSheet(u"QPushButton{\n"
"	\n"
"	\n"
"	background-color: rgb(200, 200, 200);\n"
"  	border: 2px solid rgb(132, 132, 132);\n"
"  	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: rgb(255, 255, 255);\n"
"  border: 3px solid rgb(102, 102, 102);\n"
"  border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: rgb(200, 200, 200);\n"
"  border: 3px solid rgb(102, 102, 102);\n"
"  border-radius: 5px;\n"
"}")

        self.horizontalLayout_6.addWidget(self.InsertemLotes)

        self.Salvar = QPushButton(self.frame)
        self.Salvar.setObjectName(u"Salvar")
        self.Salvar.setMinimumSize(QSize(0, 50))
        self.Salvar.setFont(font1)
        self.Salvar.setCursor(QCursor(Qt.PointingHandCursor))
        self.Salvar.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(200, 200, 200);\n"
"  	border: 2px solid rgb(132, 132, 132);\n"
"  	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: rgb(255, 255, 255);\n"
"  border: 3px solid rgb(102, 102, 102);\n"
"  border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: rgb(200, 200, 200);\n"
"  border: 3px solid rgb(102, 102, 102);\n"
"  border-radius: 5px;\n"
"}")

        self.horizontalLayout_6.addWidget(self.Salvar)


        self.verticalLayout_15.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_2 = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_2)


        self.horizontalLayout_8.addLayout(self.verticalLayout_15)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_5.addItem(self.verticalSpacer_6)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_5)


        self.verticalLayout_16.addLayout(self.horizontalLayout_8)


        self.verticalLayout_17.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.Pages.addWidget(self.CadastroUsuario)
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
        self.widget.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.5);")
        self.verticalLayout_13 = QVBoxLayout(self.widget)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_6 = QSpacerItem(1047, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_13.addItem(self.horizontalSpacer_6)

        self.verticalSpacer_3 = QSpacerItem(20, 183, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(3, 3, 3, 3)
        self.EnvioDeAvisos = QLabel(self.widget)
        self.EnvioDeAvisos.setObjectName(u"EnvioDeAvisos")
        self.EnvioDeAvisos.setFont(font1)
        self.EnvioDeAvisos.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_12.addWidget(self.EnvioDeAvisos)

        self.CentralAvisos = QPushButton(self.widget)
        self.CentralAvisos.setObjectName(u"CentralAvisos")
        self.CentralAvisos.setMinimumSize(QSize(200, 200))
        self.CentralAvisos.setCursor(QCursor(Qt.PointingHandCursor))
        self.CentralAvisos.setStyleSheet(u"QPushButton{\n"
"	image: url(:/home/Icons/aviso.png);\n"
"	background-color: rgb(200, 200, 200);\n"
"  	border: 4px solid rgb(132, 132, 132);\n"
"  	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: rgb(255, 255, 255);\n"
"  border: 5px solid rgb(102, 102, 102);\n"
"  border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: rgb(200, 200, 200);\n"
"  border: 3px solid rgb(102, 102, 102);\n"
"  border-radius: 5px;\n"
"}")

        self.verticalLayout_12.addWidget(self.CentralAvisos)


        self.horizontalLayout_3.addLayout(self.verticalLayout_12)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(3, 3, 3, 3)
        self.CadastroUsuarios = QLabel(self.widget)
        self.CadastroUsuarios.setObjectName(u"CadastroUsuarios")
        self.CadastroUsuarios.setFont(font1)
        self.CadastroUsuarios.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_11.addWidget(self.CadastroUsuarios)

        self.CadastrarUsuario = QPushButton(self.widget)
        self.CadastrarUsuario.setObjectName(u"CadastrarUsuario")
        self.CadastrarUsuario.setMinimumSize(QSize(200, 200))
        self.CadastrarUsuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.CadastrarUsuario.setStyleSheet(u"QPushButton{\n"
"	image: url(:/home/Icons/do-utilizador.png);\n"
"	background-color: rgb(200, 200, 200);\n"
"  	border: 4px solid rgb(132, 132, 132);\n"
"  	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: rgb(255, 255, 255);\n"
"  border: 5px solid rgb(102, 102, 102);\n"
"  border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: rgb(200, 200, 200);\n"
"  border: 3px solid rgb(102, 102, 102);\n"
"  border-radius: 5px;\n"
"}")

        self.verticalLayout_11.addWidget(self.CadastrarUsuario)


        self.horizontalLayout_3.addLayout(self.verticalLayout_11)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(3, 3, 3, 3)
        self.ArquivoEnvio = QLabel(self.widget)
        self.ArquivoEnvio.setObjectName(u"ArquivoEnvio")
        self.ArquivoEnvio.setFont(font1)
        self.ArquivoEnvio.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_10.addWidget(self.ArquivoEnvio)

        self.FileUpload = QPushButton(self.widget)
        self.FileUpload.setObjectName(u"FileUpload")
        self.FileUpload.setMinimumSize(QSize(200, 200))
        self.FileUpload.setCursor(QCursor(Qt.PointingHandCursor))
        self.FileUpload.setStyleSheet(u"QPushButton{\n"
"	image: url(:/home/Icons/envio.png);\n"
"	background-color: rgb(200, 200, 200);\n"
"  	border: 4px solid rgb(132, 132, 132);\n"
"  	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: rgb(255, 255, 255);\n"
"  border: 5px solid rgb(102, 102, 102);\n"
"  border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: rgb(200, 200, 200);\n"
"  border: 3px solid rgb(102, 102, 102);\n"
"  border-radius: 5px;\n"
"}")

        self.verticalLayout_10.addWidget(self.FileUpload)


        self.horizontalLayout_3.addLayout(self.verticalLayout_10)


        self.verticalLayout_13.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 183, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_4)

        self.horizontalSpacer_5 = QSpacerItem(1047, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_13.addItem(self.horizontalSpacer_5)

        self.tabWidget.addTab(self.widget, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), u"")

        self.horizontalLayout_2.addWidget(self.tabWidget)

        self.Pages.addWidget(self.MenuPrincipal)

        self.horizontalLayout.addWidget(self.Pages)

        CrawTo.setCentralWidget(self.centralwidget)

        self.retranslateUi(CrawTo)

        self.Pages.setCurrentIndex(1)
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
        self.label.setText(QCoreApplication.translate("CrawTo", u"Tipo De Usu\u00e1rio", None))
        self.UsuarioTipo.setItemText(0, "")
        self.UsuarioTipo.setItemText(1, QCoreApplication.translate("CrawTo", u"Administrador", None))
        self.UsuarioTipo.setItemText(2, QCoreApplication.translate("CrawTo", u"Usu\u00e1rio Padr\u00e3o", None))

        self.SenhaDeAcesso.setText(QCoreApplication.translate("CrawTo", u"SENHA DE ACESSO", None))
        self.label_2.setText(QCoreApplication.translate("CrawTo", u"REPETIR SENHA", None))
        self.InsertemLotes.setText(QCoreApplication.translate("CrawTo", u"Cadastro em Lotes", None))
        self.Salvar.setText(QCoreApplication.translate("CrawTo", u"Salvar Altera\u00e7\u00f5es", None))
        self.EnvioDeAvisos.setText(QCoreApplication.translate("CrawTo", u"Envio De Avisos", None))
        self.CentralAvisos.setText("")
#if QT_CONFIG(tooltip)
        self.CadastroUsuarios.setToolTip(QCoreApplication.translate("CrawTo", u"<html><head/><body><p align=\"center\">Cadastro de Usu\u00e1rios</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.CadastroUsuarios.setText(QCoreApplication.translate("CrawTo", u"Cadastro de Usu\u00e1rios", None))
        self.CadastrarUsuario.setText("")
        self.ArquivoEnvio.setText(QCoreApplication.translate("CrawTo", u"File Upload", None))
        self.FileUpload.setText("")
    # retranslateUi

