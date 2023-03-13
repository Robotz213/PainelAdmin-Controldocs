import mysql.connector

class ConnectDB:
    def __mysql__(self):
        DATABASE = 'crawjud-controle_processual'
        HOST = 'localhost'
        PORT = '8006'
        USER = 'root'
        PASSWORD = 'A219358$b'


        conexao = mysql.connector.connect(

            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )
        
        return conexao
        