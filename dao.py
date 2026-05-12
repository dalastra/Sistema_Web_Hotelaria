import pymysql

def conectar():
    conexao = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="hotelaria"
    )

    return conexao