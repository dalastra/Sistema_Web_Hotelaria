from dao import conectar

def add_hospede(nome, email, telefone, cpf):
    conexao = conectar()

    cursor = conexao.cursor()

    comando = """
    INSERT INTO hospedes (nome, email, telefone, cpf)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(comando, (nome, email, telefone, cpf))

    conexao.commit()

    cursor.close()
    conexao.close()

def consulta_hospedes():
    conexao = conectar()

    cursor = conexao.cursor()

    comando = "SELECT * FROM hospedes"

    cursor.execute(comando)

    dados = cursor.fetchall()

    cursor.close()
    conexao.close()

    return dados

def consulta_hospede_id(id):

    conexao = conectar()

    cursor = conexao.cursor()

    comando = "SELECT * FROM hospedes WHERE id = %s"

    cursor.execute(comando, (id,))

    hospede = cursor.fetchone()

    cursor.close()
    conexao.close()

    return hospede

def update_hospede(id, nome, email, telefone, cpf):

    conexao = conectar()

    cursor = conexao.cursor()

    comando = """
    UPDATE hospedes
    SET nome = %s,
        email = %s,
        telefone = %s,
        cpf = %s
    WHERE id = %s
    """

    cursor.execute(
        comando,
        (nome, email, telefone, cpf, id)
    )

    conexao.commit()

    cursor.close()
    conexao.close()

def delete_hospede(id):

    conexao = conectar()

    cursor = conexao.cursor()

    comando = "DELETE FROM hospedes WHERE id = %s"

    cursor.execute(comando, (id,))

    conexao.commit()

    cursor.close()
    conexao.close()