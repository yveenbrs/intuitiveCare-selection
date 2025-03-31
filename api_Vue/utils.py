import os
import csv

def read_csv(csv_file):
    """
    Função responsável por fazer a leitura do arquivo csv, transformando-o em uma lista.
    """
    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=";")
        next(reader, None)
        data_list = [row for row in reader]
    return data_list
