import mysql.connector
import os
import pandas as pd
import re


def get_mysql_connection():
    try:
        conn = mysql.connector.connect(host="localhost", user="root", password="1234")
        return conn
    except mysql.connector.Error as err:
        print(f"Erro de conexão: {err}")
        raise


def read_sql_query(query_path):
    with open(query_path, "r") as file:
        return file.read()


def row_to_insert(row):
    float_pattern = r"^[+-]?[0-9,\.]+$"

    result = []
    for column in row.index:
        value = row[column]

        if pd.isna(value):
            value = None
        elif type(value) == str and re.match(float_pattern, value):
            value = value.replace(",", ".")
        else:
            value = str(value)
        value = value.strip()
        result.append(value)

    return result


def insert_from_dataframe(dataframe_path, insert_query, cursor):
    dataframe_name = os.path.basename(dataframe_path)
    print(f'\nIniciou inserção do "{dataframe_name}"...')

    dataframe = pd.read_csv(dataframe_path, sep=";")
    dataframe_length = len(dataframe)

    for i in range(dataframe_length):
        try:
            cursor.execute(
                read_sql_query(insert_query),
                row_to_insert(dataframe.iloc[i])
                )

            if (i + 1) == 1 or (i + 1) % 5000 == 0 or (i + 1) == dataframe_length:
                print(f"{i+1}/{dataframe_length}")
        except Exception as error:
            print(f"Error ao inserir a linha {i+1}: {row_to_insert(dataframe.iloc[i])}")

    print(f'Finalizou inserção do "{dataframe_name}".')