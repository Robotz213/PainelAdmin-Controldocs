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
        self.AcessoPessoas = QPushButton(self.Dockbar)
        self.AcessoPessoas.setObjectName(u"AcessoPessoas")
        self.AcessoPessoas.setMinimumSize(QSize(48, 50))
        self.AcessoPessoas.setMaximumSize(QSize(50, 50))
        self.AcessoPessoas.setStyleSheet(u"QPushButton{\n"
"	\n"
"	image: url(:/home/Icons/do-utilizador.png);\n"
"	background-color: rgba(255, 255, 255, 0.5);\n"
"}\n"
"\n"
"QPushButton:hoved{\n"
"	background-color: rgba(162, 162, 162, 0.3);\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.AcessoPessoas)

        self.Processos = QPushButton(self.Dockbar)
        self.Processos.setObjectName(u"Processos")
        self.Processos.setEnabled(True)
        self.Processos.setMinimumSize(QSize(48, 50))
        self.Processos.setMaximumSize(QSize(50, 50))
        self.Processos.setCursor(QCursor(Qt.PointingHandCursor))
        self.Processos.setLayoutDirection(Qt.LeftToRight)
        self.Processos.setStyleSheet(u"QPushButton{\n"
"\n"
"	image: url(:/home/Icons/documento.png);\n"
"	background-color: rgba(255, 255, 255, 0.5);\n"
"}\n"
"\n"
"QPushButton:hoved{\n"
"	background-color: rgba(162, 162, 162, 0.3);\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.Processos)

        self.Prazos = QPushButton(self.Dockbar)
        self.Prazos.setObjectName(u"Prazos")
        self.Prazos.setMinimumSize(QSize(48, 50))
        self.Prazos.setMaximumSize(QSize(50, 50))
        self.Prazos.setCursor(QCursor(Qt.PointingHandCursor))
        self.Prazos.setStyleSheet(u"QPushButton{\n"
"	image: url(:/home/Icons/caderno.png);\n"
"	background-color: rgba(255, 255, 255, 0.5);\n"
"}\n"
"\n"
"QPushButton:hoved{\n"
"	background-color: rgba(162, 162, 162, 0.3);\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.Prazos)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.UsersConfig = QPushButton(self.Dockbar)
        self.UsersConfig.setObjectName(u"UsersConfig")
        self.UsersConfig.setMinimumSize(QSize(48, 50))
        self.UsersConfig.setMaximumSize(QSize(50, 50))
        self.UsersConfig.setStyleSheet(u"QPushButton{\n"
"\n"
"	\n"
"	image: url(:/home/Icons/simbolo-de-interface-da-roda-dentada-de-configuracao.png);\n"
"	background-color: rgba(255, 255, 255, 0.5);\n"
"}\n"
"\n"
"QPushButton:hoved{\n"
"	background-color: rgba(162, 162, 162, 0.3);\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.UsersConfig)

        self.Info = QPushButton(self.Dockbar)
        self.Info.setObjectName(u"Info")
        self.Info.setMinimumSize(QSize(48, 50))
        self.Info.setMaximumSize(QSize(50, 50))
        self.Info.setCursor(QCursor(Qt.PointingHandCursor))
        self.Info.setStyleSheet(u"QPushButton{\n"
"image: url(:/home/Icons/informacoes.png);\n"
"background-color: rgba(255, 255, 255, 0.5);\n"
"}\n"
"\n"
"QPushButton:hoved{\n"
"background-color: rgba(162, 162, 162, 0.3);\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.Info)

        self.Sair = QPushButton(self.Dockbar)
        self.Sair.setObjectName(u"Sair")
        self.Sair.setMinimumSize(QSize(48, 50))
        self.Sair.setMaximumSize(QSize(45, 50))
        self.Sair.setCursor(QCursor(Qt.PointingHandCursor))
        self.Sair.setStyleSheet(u"QPushButton{\n"
"	\n"
"	image: url(:/home/Icons/sair.png);\n"
"background-color: rgba(255, 255, 255, 0.5);\n"
"}\n"
"\n"
"QPushButton:hoved{\n"
"background-color: rgba(162, 162, 162, 0.3);\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.Sair)


        self.horizontalLayout.addWidget(self.Dockbar)

        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        self.Sobre = QWidget()
        self.Sobre.setObjectName(u"Sobre")
        self.Pages.addWidget(self.Sobre)
        self.Pessoas = QWidget()
        self.Pessoas.setObjectName(u"Pessoas")
        self.Pages.addWidget(self.Pessoas)
        self.Processos_Lista = QWidget()
        self.Processos_Lista.setObjectName(u"Processos_Lista")
        self.horizontalLayout_2 = QHBoxLayout(self.Processos_Lista)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.Processos_Lista)
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
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.InsertProcesso = QLineEdit(self.frame)
        self.InsertProcesso.setObjectName(u"InsertProcesso")
        self.InsertProcesso.setMinimumSize(QSize(100, 40))
        self.InsertProcesso.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(15)
        self.InsertProcesso.setFont(font)
        self.InsertProcesso.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.InsertProcesso)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.EnterCadastro = QPushButton(self.frame)
        self.EnterCadastro.setObjectName(u"EnterCadastro")
        self.EnterCadastro.setMinimumSize(QSize(200, 60))
        font1 = QFont()
        font1.setPointSize(12)
        self.EnterCadastro.setFont(font1)

        self.verticalLayout_3.addWidget(self.EnterCadastro)

        self.reload = QPushButton(self.frame)
        self.reload.setObjectName(u"reload")
        self.reload.setMinimumSize(QSize(200, 60))
        self.reload.setFont(font1)

        self.verticalLayout_3.addWidget(self.reload)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.TabelaProcesso = QTreeWidget(self.widget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setFont(8, font1);
        __qtreewidgetitem.setFont(7, font1);
        __qtreewidgetitem.setFont(6, font1);
        __qtreewidgetitem.setFont(5, font1);
        __qtreewidgetitem.setFont(4, font1);
        __qtreewidgetitem.setFont(3, font1);
        __qtreewidgetitem.setFont(2, font1);
        __qtreewidgetitem.setFont(1, font1);
        __qtreewidgetitem.setTextAlignment(0, Qt.AlignLeading|Qt.AlignVCenter);
        __qtreewidgetitem.setFont(0, font1);
        self.TabelaProcesso.setHeaderItem(__qtreewidgetitem)
        self.TabelaProcesso.setObjectName(u"TabelaProcesso")
        self.TabelaProcesso.setStyleSheet(u"background-color: rgb(221, 221, 221);")

        self.gridLayout.addWidget(self.TabelaProcesso, 2, 0, 1, 1)

        self.progressBar = QProgressBar(self.widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 1)

        self.tabWidget.addTab(self.widget, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), u"")

        self.horizontalLayout_2.addWidget(self.tabWidget)

        self.Pages.addWidget(self.Processos_Lista)
        self.Agenda = QWidget()
        self.Agenda.setObjectName(u"Agenda")
        self.Pages.addWidget(self.Agenda)

        self.horizontalLayout.addWidget(self.Pages)

        CrawTo.setCentralWidget(self.centralwidget)

        self.retranslateUi(CrawTo)

        self.Pages.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(CrawTo)
    # setupUi

    def retranslateUi(self, CrawTo):
        CrawTo.setWindowTitle(QCoreApplication.translate("CrawTo", u"MainWindow", None))
        self.AcessoPessoas.setText("")
        self.Processos.setText("")
        self.Prazos.setText("")
        self.UsersConfig.setText("")
        self.Info.setText("")
        self.Sair.setText("")
        self.InsertProcesso.setText("")
        self.EnterCadastro.setText(QCoreApplication.translate("CrawTo", u"Cadastrar Processo", None))
        self.reload.setText(QCoreApplication.translate("CrawTo", u"Filtrar", None))
        ___qtreewidgetitem = self.TabelaProcesso.headerItem()
        ___qtreewidgetitem.setText(8, QCoreApplication.translate("CrawTo", u"Data De Cadastro", None));
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("CrawTo", u"Status do Processo", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("CrawTo", u"Data Distribui\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("CrawTo", u"Valor Da Causa", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("CrawTo", u"Advogado R\u00e9u", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("CrawTo", u"R\u00e9u", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("CrawTo", u"Advogado Autor", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("CrawTo", u"Autor", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("CrawTo", u"N\u00ba Processo", None));
    # retranslateUi

