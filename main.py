from PySide2.QtWidgets import(QApplication, QFileDialog,
 QMainWindow, QMessageBox, QTreeWidgetItem, QWidget)
from PySide2 import QtCore
from PySide2.QtGui import QIcon

import sys, os
import requests
 
from tkinter import *
from tkinter.messagebox import askyesno
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo

from time import sleep
from Scripts.ui_main import Ui_CrawTo
from Scripts.ui_login import Ui_Form
from Scripts.ui_cadastroemlotes import Ui_Cadastro
from Scripts.ui_sendavisos import Ui_Avisos
from Scripts.ui_uploadfiles import Ui_Upload

from hashlib import sha512


import json
from Config.sqlconfig import ConnectDB
import pandas as pd
import pathlib
from Scripts.ui_cadastroemlotes import Ui_Cadastro




class Login(QWidget, Ui_Form):
    
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.setupUi(self)
        diricon = os.path.join(os.getcwd(),'Icons','faviconproexpress.png')
        self.setWindowIcon(QIcon(diricon))
        self.setWindowTitle("ControlDocs - Proexpress")

        self.EnterButton.clicked.connect(self.opensys)

    def opensys(self):


        conexao = ConnectDB().__mysql__()
        startDB = conexao.cursor()

        usuáriologado = self.UserFrame.text()
        try:
            checkuser = f'SELECT user FROM users WHERE user = "{self.UserFrame.text()}"'
            startDB.execute(checkuser)
            user = startDB.fetchall()
            usuáriologado = user
            if self.UserFrame.text() in user[0]:
                try:
                    hashed_password = sha512(self.PasswordFrame.text().encode()).hexdigest()
                    checkpassword = f'SELECT password FROM users WHERE user = "{self.UserFrame.text()}"'
                    startDB.execute(checkpassword)
                    password = startDB.fetchall()
                    pass_word = password[0]
                    if hashed_password in pass_word:
                        self.w = MainWindow()
                        self.w.show()
                        self.close()
                        
                            

                except Exception as e:
                    showerror('Erro', 'Usuário ou Senha incorretos')
                    conexao.close()
                    print(e)

            
        except Exception as e:
            showerror('Erro', 'Usuário ou Senha incorretos')
            conexao.close()
            print(e)

        

class MainWindow(QMainWindow, Ui_CrawTo):

    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("ControlDocs - Proexpress")
        diricon = os.path.join(os.getcwd(),'Icons','faviconproexpress.png')
        self.setWindowIcon(QIcon(diricon))

        ## Janelas do Aplicativo
        self.retornar.clicked.connect(lambda: self.Pages.setCurrentWidget(self.MenuPrincipal))
        self.CadastrarUsuario.clicked.connect(lambda: self.cadlotes)
        self.FileUpload.clicked.connect(lambda: self.uploadfiles)
        self.CentralAvisos.clicked.connect(lambda: self.avisolot)


        ## Fechar Aplicação
        self.Sair.clicked.connect(lambda: self.exitapp())
        self.InsertemLotes.clicked.connect(lambda: self.cadastraremlotes())
        


    def exitapp(self):
        answer = askyesno(title='Confirmação',message='Quer Realmente Sair?')
        if answer is True:
            conexao = ConnectDB().__mysql__()
            conexao.close()

            sys.exit()

    def cadlotes(self):

        self.w = CadastroEmLotes()
        self.w.show()

    def avisolot(self):

        self.w = CentralDeAvisos()
        self.w.show()

    def uploadfiles(self):
        self.w = Uploadfiles()
        self.w.show()

        

class CadastroEmLotes(QWidget, Ui_Cadastro):
    def __init__(self) -> None:
        super(CadastroEmLotes, self).__init__()
        diricon = os.path.join(os.getcwd(),'Icons','faviconproexpress.png')
        self.setWindowIcon(QIcon(diricon))
        self.setupUi(self)
        self.setWindowTitle("ControlDocs - Proexpress")

class CentralDeAvisos(QWidget, Ui_Avisos):
    def __init__(self) -> None:
        super(CentralDeAvisos, self).__init__()
        diricon = os.path.join(os.getcwd(),'Icons','faviconproexpress.png')
        self.setWindowIcon(QIcon(diricon))
        self.setupUi(self)
        self.setWindowTitle("ControlDocs - Proexpress")

class Uploadfiles(QWidget, Ui_Upload):
    def __init__(self) -> None:
        super(Uploadfiles, self).__init__()
        diricon = os.path.join(os.getcwd(),'Icons','faviconproexpress.png')
        self.setWindowIcon(QIcon(diricon))
        self.setupUi(self)
        self.setWindowTitle("ControlDocs - Proexpress")




        
    #def openpath(self)
        
   
if __name__ == "__main__":
    
    
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()
    