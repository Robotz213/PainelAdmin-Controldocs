from PySide2.QtWidgets import(QApplication, QFileDialog,
 QMainWindow, QMessageBox, QTreeWidgetItem, QWidget)
from PySide2 import QtCore
from PySide2.QtGui import QIcon

import sys
import requests
 
from tkinter import *
from tkinter.messagebox import askyesno
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo

from time import sleep
from Scripts.ui_main import Ui_CrawTo
from Scripts.ui_login import Ui_Form
from hashlib import sha512


import json
from Config.sqlconfig import ConnectDB
import pandas as pd
import pathlib





class Login(QWidget, Ui_Form, ):
    
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Login CrawJUD')

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
                        
                        with open(pathlib.Path(__file__).parent.resolve()/"logfile.txt", "w") as f:
                            sleep(2)
                            f.write(self.UserFrame.text())
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
        self.setWindowTitle("CrawJUD - Gestão Processual")

        ## Janelas do Aplicativo
        
        self.Info.clicked.connect(lambda: self.Pages.setCurrentWidget(self.Sobre))
        self.Processos.clicked.connect(lambda: self.Pages.setCurrentWidget(self.Processos_Lista))
        self.Prazos.clicked.connect(lambda: self.Pages.setCurrentWidget(self.Agenda))
        self.UsersConfig.clicked.connect(lambda: self.newuser())
        self.EnterCadastro.clicked.connect(lambda: self.searchproc())
        self.reload.clicked.connect(lambda: self.reset_table())
    ## Fechar Aplicação
        self.Sair.clicked.connect(lambda: self.exitapp())
        self.progressBar
        


    def exitapp(self):
        answer = askyesno(title='Confirmação',message='Quer Realmente Sair?')
        if answer is True:
            conexao = ConnectDB().__mysql__()
            conexao.close()

            sys.exit()


        
if __name__ == "__main__":
    
    
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()
    