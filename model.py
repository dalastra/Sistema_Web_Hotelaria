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
        (
            nome,
            email,
            telefone,
            cpf,
            id
        )
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
    
def consulta_quartos():

    conexao = conectar()

    cursor = conexao.cursor()

    comando = "SELECT * FROM quartos"

    cursor.execute(comando)

    quartos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return quartos

def add_quarto(numero, tipo, valor_diaria, status):

    conexao = conectar()

    cursor = conexao.cursor()

    comando = """
    INSERT INTO quartos
    (numero, tipo, valor_diaria, status)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(
        comando,
        (numero, tipo, valor_diaria, status)
    )

    conexao.commit()

    cursor.close()
    conexao.close()

def consulta_quarto_id(id):

    conexao = conectar()

    cursor = conexao.cursor()

    comando = "SELECT * FROM quartos WHERE id = %s"

    cursor.execute(comando, (id,))

    quarto = cursor.fetchone()

    cursor.close()
    conexao.close()

    return quarto

def update_quarto(id, numero, tipo, valor_diaria, status):

    conexao = conectar()

    cursor = conexao.cursor()

    comando = """
    UPDATE quartos
    SET numero = %s,
        tipo = %s,
        valor_diaria = %s,
        status = %s
    WHERE id = %s
    """

    cursor.execute(
        comando,
        (numero, tipo, valor_diaria, status, id)
    )

    conexao.commit()

    cursor.close()
    conexao.close()

def delete_quarto(id):

    conexao = conectar()

    cursor = conexao.cursor()

    comando = "DELETE FROM quartos WHERE id = %s"

    cursor.execute(comando, (id,))

    conexao.commit()

    cursor.close()
    conexao.close()

def consulta_reservas():

    conexao = conectar()

    cursor = conexao.cursor()

    comando = """
    SELECT
        reservas.id,
        hospedes.nome,
        quartos.numero,
        reservas.data_entrada,
        reservas.data_saida

    FROM reservas

    INNER JOIN hospedes
        ON reservas.hospede_id = hospedes.id

    INNER JOIN quartos
        ON reservas.quarto_id = quartos.id
    """

    cursor.execute(comando)

    reservas = cursor.fetchall()

    cursor.close()
    conexao.close()

    return reservas

def add_reserva(
    hospede_id,
    quarto_id,
    data_entrada,
    data_saida
):

    conexao = conectar()

    cursor = conexao.cursor()

    comando = """
    INSERT INTO reservas
    (hospede_id, quarto_id, data_entrada, data_saida)

    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(
        comando,
        (
            hospede_id,
            quarto_id,
            data_entrada,
            data_saida
        )
    )

    conexao.commit()

    cursor.close()
    conexao.close()

def delete_reserva(id):

    conexao = conectar()

    cursor = conexao.cursor()

    comando = "DELETE FROM reservas WHERE id = %s"

    cursor.execute(comando, (id,))

    conexao.commit()

    cursor.close()
    conexao.close()

def consulta_reserva_id(id):

    conexao = conectar()

    cursor = conexao.cursor()

    comando = """
    SELECT
        reservas.id,
        hospedes.nome,
        hospedes.email,
        hospedes.telefone,
        quartos.numero,
        quartos.tipo,
        quartos.valor_diaria,
        reservas.data_entrada,
        reservas.data_saida

    FROM reservas

    INNER JOIN hospedes
        ON reservas.hospede_id = hospedes.id

    INNER JOIN quartos
        ON reservas.quarto_id = quartos.id

    WHERE reservas.id = %s
    """

    cursor.execute(comando, (id,))

    reserva = cursor.fetchone()

    cursor.close()
    conexao.close()

    return reserva

def consulta_reserva_id_edit(id):

    conexao = conectar()

    cursor = conexao.cursor()

    comando = "SELECT * FROM reservas WHERE id = %s"

    cursor.execute(comando, (id,))

    reserva = cursor.fetchone()

    cursor.close()
    conexao.close()

    return reserva

def update_reserva(
    id,
    hospede_id,
    quarto_id,
    data_entrada,
    data_saida
):

    conexao = conectar()

    cursor = conexao.cursor()

    comando = """
    UPDATE reservas
    SET hospede_id = %s,
        quarto_id = %s,
        data_entrada = %s,
        data_saida = %s
    WHERE id = %s
    """

    cursor.execute(
        comando,
        (
            hospede_id,
            quarto_id,
            data_entrada,
            data_saida,
            id
        )
    )

    conexao.commit()

    cursor.close()
    conexao.close()