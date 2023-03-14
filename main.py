from PySide2.QtWidgets import(QApplication, QFileDialog,
 QMainWindow, QMessageBox, QTreeWidgetItem, QWidget)
from PySide2 import QtCore
from PySide2.QtGui import QIcon
from datetime import datetime
from PyQt5 import QtWidgets

import sys, os
import openpyxl
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
from tkinter import filedialog as fd


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

        
        startDB.execute(f'SELECT user FROM users WHERE user = "{self.UserFrame.text()}"')
        user = startDB.fetchall()

        startDB.execute(f'SELECT cpf FROM users WHERE cpf = "{self.UserFrame.text()}"')
        cpf = startDB.fetchall()



        if self.UserFrame.text() in user:
            try:
                hashed_password = sha512(self.PasswordFrame.text().encode()).hexdigest()
                checkpassword = f'SELECT password FROM users WHERE user = "{self.UserFrame.text()}"'
                startDB.execute(checkpassword)
                password = startDB.fetchall()
                pass_word = password[0]
                if hashed_password in pass_word:
                    self.w = MainWindow()
                    logintime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # registra data e hora do login

                    # atualiza a coluna login_time na tabela users com a hora de login
                    startDB.execute("UPDATE users SET login_time = %s WHERE user = %s", [logintime, self.UserFrame.text()])
                    conexao.commit()
                    self.w.show()
                    self.close()

            except Exception as e:
                showerror('Erro', 'Senha incorreta')
                conexao.close()
                print(e)

        elif self.UserFrame.text() in cpf:
            try:
                hashed_password = sha512(self.PasswordFrame.text().encode()).hexdigest()
                checkpassword = f'SELECT password FROM users WHERE cpf = "{self.UserFrame.text()}"'
                startDB.execute(checkpassword)
                password = startDB.fetchall()
                pass_word = password[0]
                if hashed_password in pass_word:
                    self.w = MainWindow()
                    logintime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # registra data e hora do login

                    # atualiza a coluna login_time na tabela users com a hora de login
                    startDB.execute("UPDATE users SET login_time = %s WHERE user = %s", [logintime, self.UserFrame.text()])
                    conexao.commit()
                    self.w.show()
                    self.close()
            except Exception as e:
                showerror('Erro', 'Senha incorreta')
                conexao.close()
                print(e)

        else:
            showerror('ERRO', 'Usuário não encontrado') 

                            

                

            
        

        

class MainWindow(QMainWindow, Ui_CrawTo):

    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("ControlDocs - Proexpress")
        diricon = os.path.join(os.getcwd(),'Icons','faviconproexpress.png')
        self.setWindowIcon(QIcon(diricon))

        ## Janelas do Aplicativo
        self.retornar.clicked.connect(lambda: self.Pages.setCurrentWidget(self.MenuPrincipal))
        self.CadastrarUsuario.clicked.connect(lambda: self.Pages.setCurrentWidget(self.CadastroUsuario))
        self.FileUpload.clicked.connect(lambda: self.uploadfiles())
        self.CentralAvisos.clicked.connect(lambda: self.avisolot())
        self.InsertemLotes.clicked.connect(lambda: self.cadlotes())
        
        ##Cadastrar Usuário
        self.Salvar.clicked.connect(lambda: self.cadusuario())


        ## Fechar Aplicação
        self.Sair.clicked.connect(lambda: self.exitapp())
        
        


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

    def cadusuario(self):


        conexao = ConnectDB().__mysql__()
        startDB = conexao.cursor()

        NomeUsuario = self.lineNome.text()
        cpf = self.lineCPF.text()
        email = self.lineMails.text()
        Funcao = self.lineFuncao.text()
        matricula = self.lineMatricula.text()

        senha = self.lineSenha.text()
        confirmsenha = self.lineEdit_2.text()
        
        infotocat = [NomeUsuario, cpf, email,Funcao, matricula]
        bypassPW = [senha, confirmsenha]


        if bypassPW[0] != bypassPW[1]:
            showerror('ERRO', 'Senhas não conferem')
        else:
            hashedPW = sha512(bypassPW[0].encode()).hexdigest()
            startDB.execute(f'INSERT INTO users (user, cpf, email, password, funcao, matricula) VALUES ("{infotocat[0]}", "{infotocat[1]}", "{infotocat[2]}", "{hashedPW}", "{infotocat[3]}", "{infotocat[4]}")')
            conexao.commit()

            showinfo('SUCESSO', 'Usuário cadastrado com sucesso')



        

class CadastroEmLotes(QWidget, Ui_Cadastro):
    def __init__(self) -> None:
        super(CadastroEmLotes, self).__init__()
        diricon = os.path.join(os.getcwd(),'Icons','faviconproexpress.png')
        self.setWindowIcon(QIcon(diricon))
        self.setupUi(self)
        self.setWindowTitle("ControlDocs - Proexpress")

        self.BuscarPlanilha.clicked.connect(lambda: self.openfile())
        self.IniciarCadastro.clicked.connect(lambda: self.initcadastro(input_filename=self.lineEndr.text()))

    
    def openfile(self):
        input_filename = QtWidgets.QFileDialog.getOpenFileName()[0]
        self.lineEndr.setText(input_filename)
                

    def initcadastro(self, input_filename):
        conexao = ConnectDB().__mysql__()
        startDB = conexao.cursor()
        
        
        wrkbk_input = openpyxl.load_workbook(filename=input_filename)
        sheet_input = wrkbk_input.active

        for i in range(2, sheet_input.max_row+1):
            cell_obj = sheet_input.cell(row=i, column=1)
            if cell_obj.value is not None and cell_obj.value != '':
                matricula = cell_obj.value.replace(' ','')
                funcionario = sheet_input.cell(row=i, column=2).value
                CPF = sheet_input.cell(row=i, column=3).value
                funcao = sheet_input.cell(row=i, column=4).value
                try:
                    email = sheet_input.cell(row=i, column=5).value
                except:
                    email = ''
                try:
                    senha = sheet_input.cell(row=i, column=6).value
                except:
                    senha = ''

                infotocat = [matricula, funcionario, CPF, funcao, email, senha]

                if infotocat[5] is None:
                    showerror('ERRO', 'Usuário para cadastro da linha nº{} não possui senha informada'.format(i))
                    break

                elif infotocat[4] is None:
                    try:
                        hashedPW = sha512(infotocat[5].encode()).hexdigest()
                        startDB.execute(f'INSERT INTO users (user, cpf, password, funcao, matricula) VALUES ("{infotocat[1]}", "{infotocat[2]}", "{hashedPW}", "{infotocat[3]}", "{infotocat[0]}")')
                        conexao.commit()

                    except Exception as e:
                        print(e)
                else:
                    try:
                        hashedPW = sha512(senha.encode()).hexdigest()
                        startDB.execute(f'INSERT INTO users (user, cpf, email, password, funcao, matricula) VALUES ("{infotocat[1]}", "{infotocat[2]}", "{infotocat[4]}", "{hashedPW}", "{infotocat[3]}", "{infotocat[0]}")')
                        conexao.commit()

                    except Exception as e:
                        print(e)

                    
            if i == sheet_input.max_row:
                showinfo('SUCESSO', 'Usuários Cadastrados com sucesso')


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
    