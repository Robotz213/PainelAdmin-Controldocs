from PySide2.QtWidgets import(QApplication, QFileDialog,
 QMainWindow, QMessageBox, QTreeWidgetItem, QWidget)
from PySide2 import QtCore
from PySide2.QtGui import QIcon

import sys
import requests

from Scripts.esaj_capa import ESAJCrawler 
from tkinter import *
from tkinter.messagebox import askyesno
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo

from time import sleep
from Scripts.ui_main import Ui_CrawTo
from Scripts.ui_login import Ui_Form
from Scripts.ui_createuser import Ui_WindowCreateUser
from hashlib import sha512
from Config.validateactivation import ValidateKEY


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

        check_activation = ValidateKEY().checkactivation()

        if check_activation is True:

            conexao = ConnectDB().__mysql__()
            startDB = conexao.cursor()

            usuáriologado = self.UserFrame.text()
            try:
                checkuser = f'SELECT username FROM usersys WHERE username = "{self.UserFrame.text()}"'
                startDB.execute(checkuser)
                user = startDB.fetchall()
                usuáriologado = user
                if self.UserFrame.text() in user[0]:
                    try:
                        checkpassword = f'SELECT username, password FROM usersys WHERE username = "{self.UserFrame.text()}"'
                        startDB.execute(checkpassword)
                        password = startDB.fetchall()
                        if self.PasswordFrame.text() in password[0]:
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

        else:
            showerror('Erro Fatal', 'Acesso ao sistema Bloqueado por REMINFOTECH')
            self.close()

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
        

    def searchproc(self):
        
        self.progressBar.setValue(0)
        


        for i in range(100):
            sleep(0.11)
            self.progressBar.setValue(i)
  
            if i > 98 :
            
                self.progressBar.setValue(i)
                sleep(0.01)
                self.progressBar.setValue(99)
                self.progressBar.setValue(99)
                
                searchprocesso = ESAJCrawler().initcrawler(processonumber=self.InsertProcesso.text())
                if searchprocesso is True:
                    self.progressBar.setValue(100)
                    showinfo('Sucesso', 'Processo Cadastrado com sucesso!')
                    self.reset_table()
                break


    def reset_table(self):
        
        if self.InsertProcesso.text() == "":
            self.TabelaProcesso.clear()
            self.table_processos()
        else:
            self.TabelaProcesso.clear()
            conexao = ConnectDB().__mysql__()
            startDB = conexao.cursor()
            comando = f"SELECT Processo,  Autor, Advogado_Autor, Réu, Advogado_Réu, Data_Distribuição, Valor_Da_Causa, Status_Processo, Data_Cadastro FROM process_table WHERE Processo = '{self.InsertProcesso.text()}'"

            startDB.execute(comando)
            result = startDB.fetchall()


            self.TabelaProcesso.setStyleSheet(u" QHeaderView{ color:black}; font-size: 15px;")

            for i in result:
                self.campo = QTreeWidgetItem(self.TabelaProcesso, i)
                self.campo.setCheckState(0, QtCore.Qt.CheckState.Unchecked)

    def table_processos(self):
        self.TabelaProcesso.setStyleSheet(u" QHeaderView{ color:black}; font-size: 15px;")
        conexao = ConnectDB().__mysql__()
        startDB = conexao.cursor()

        comando = f"SELECT Processo, Autor, Advogado_Autor, Réu, Advogado_Réu, Data_Distribuição, Valor_Da_Causa, Status_Processo, Data_Cadastro FROM process_table"
        startDB.execute(comando)
        result = startDB.fetchall()


        for i in result:

            self.campo = QTreeWidgetItem(self.TabelaProcesso, i)
            self.campo.setCheckState(0, QtCore.Qt.CheckState.Unchecked)

    def exitapp(self):
        answer = askyesno(title='Confirmação',message='Quer Realmente Sair?')
        if answer is True:
            conexao = ConnectDB().__mysql__()
            conexao.close()

            sys.exit()

    def newuser(self):
        
        # READ
        f = open(pathlib.Path(__file__).parent.resolve()/"logfile.txt", "r")
        usuáriologado = f.read()
        print(usuáriologado)


        conexao = ConnectDB().__mysql__()
        cursor = conexao.cursor()
        comando = f'SELECT userlevel FROM usersys WHERE username = "{usuáriologado}"'

        cursor.execute(comando)
        resultado = cursor.fetchall() # ler o banco de dados


        if "Administrador" in resultado[0]:
            self.w = CreateUser()
            self.w.show()
        else:
            showerror('Bloqueio', 'Acesso não autorizado')

class CreateUser(QMainWindow, Ui_WindowCreateUser):
    
    def __init__(self) -> None:
        super(CreateUser, self).__init__()
        
        
        self.setupUi(self)
        self.setWindowTitle('Criar Usuário')

        self.Salvar.clicked.connect(lambda: self.confirmsave())
        self.Cancelar.clicked.connect(lambda: self.close())

    def confirmsave(self):
        
        ## Cadastrar Usuário
        self.NomeUsuário = self.SetNome.text()
        self.SobrenomeUsuário = self.SetSobrenome.text()

        self.Pass1 = self.SetSenha.text()
        self.Pass2 = self.SetRepeatPW.text()
        
        self.EmailUser = self.SetEmail.text()
        self.ContatoUser = self.SetContato.text()



        print(self.NomeUsuário, self.SobrenomeUsuário, self.Pass1, self.Pass2, self.EmailUser, self.ContatoUser)
        
        if self.NomeUsuário == '' or self.SobrenomeUsuário == '':
            showerror('Erro', 'Campos Nome/Sobrenome não podem ficar em branco!' )

        elif self.Pass1 != self.Pass2:
            showerror('Erro', 'Senhas não conferem')

        else:
            password = self.Pass1
        
        conexao = ConnectDB().__mysql__()
        startDB = conexao.cursor()


        userlevel = self.SetTypeUser.currentText()
        print(userlevel)

        comando = f'INSERT INTO usersys (username, lastusername, password, userlevel, email, contato) VALUES ("{self.NomeUsuário}", "{self.SobrenomeUsuário}", "{password}", "{userlevel}", "{self.EmailUser}", "{self.ContatoUser}")'

        try:
            startDB.execute(comando)
            conexao.commit()
            showinfo('Sucesso', 'Usuário Criado com Sucesso!')
        except Exception as e:
            print(e)
         # edita o banco de dados

        self.close()
        
if __name__ == "__main__":
    
    
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()
    