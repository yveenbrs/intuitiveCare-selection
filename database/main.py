import mysql.connector
import os

from utils import read_sql_query, get_mysql_connection, insert_from_dataframe

try:
    # 1. Cria uma conexao ao mysql.
    conn = get_mysql_connection()
    cursor = conn.cursor()

    # 2. Cria o banco de dados caso não exista.
    cursor.execute(read_sql_query("queries/create_database.sql"))

    # 3. Define que vamos usar o banco de dados criado anteriormente.
    cursor.execute(read_sql_query("queries/use_database.sql"))

    # 4. Cria a tabela de relatorio cadop.
    cursor.execute(read_sql_query("queries/create_table_relatorio_cadop.sql"))

    # 5. Cria a tabela de demonstracoes contabeis.
    cursor.execute(read_sql_query("queries/create_table_demonstracoes_contabeis.sql"))

    # 6. Faz um loop em todos as linhas do relatorio cadop csv e insere as linhas na tabela relatorio cadop.
    relatorio_cadop_path = "csv/relatorio-cadop/Relatorio_cadop.csv"
    insert_from_dataframe(relatorio_cadop_path, "queries/insert_into_relatorio_cadop_table.sql", cursor)

    # 7. Faz um loop em todos os arquivos contabeis lendo cada arquivo e inserindo no banco.
    contabeis_folder_path = "csv/contabeis"
    for filename in os.listdir(contabeis_folder_path):
        file_path = os.path.join(contabeis_folder_path, filename)
        insert_from_dataframe(file_path, "queries/insert_into_demonstracoes_contabeis_table.sql", cursor)
    conn.commit()

    # 8. Faz um insert para retornar os operadores com maiores despesas no último trimestre
    cursor.execute(read_sql_query("queries/select_maiores_despesas_trimestre.sql"))
    result = cursor.fetchall()
    print("Top 10 operadoras com maiores despesas no último trimestre:")
    for index, (nome, total) in enumerate(result, start=1):
        if not nome:
            nome = 'Operador sem nome'
        print(f"{index}. {nome} - Total de Despesas: R$ {total:,.2f}")
    
    # 9. Faz um insert para retornar os operadores com maiores despesas no último ano
    cursor.execute(read_sql_query("queries/select_maiores_despesas_anual.sql"))
    result = cursor.fetchall()
    print("Top 10 operadoras com maiores despesas no último ano:")
    for index, (nome, total) in enumerate(result, start=1):
        if not nome:
            nome = 'Operador sem nome'
        print(f"{index}. {nome} - Total de Despesas: R$ {total:,.2f}")

except Exception as error:
    print(error)
