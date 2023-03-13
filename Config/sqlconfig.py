import mysql.connector

class ConnectDB:
    def __mysql__(self):
        DATABASE = 'proexpress1'
        HOST = 'xmysql1.proexpress.com.br'
        USER = 'proexpress1'
        PASSWORD = 'FormularioPRO2013@'


        conexao = mysql.connector.connect(

            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )
        
        return conexao
        