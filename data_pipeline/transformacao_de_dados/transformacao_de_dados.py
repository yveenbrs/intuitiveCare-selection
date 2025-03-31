import pandas as pd
import tabula
import os

from .renamer import rename_rows
from utils.functions import compress_files

def main(output_path):
    # 1. Define as variáveis de ambiente.
    SAVE_ZIP_PATH = os.path.join(output_path, "zip")
    START_PAGE = 3
    END_PAGE = 181
    PDF_PATH = os.path.join(output_path, "pdf", "Anexo 1.pdf")

    # 2. Define caminho do arquivo para transformação

    # 3. Ler todo o PDF, salvando as tabelas em dataframe dentro de uma lista.
    table_list = tabula.read_pdf(PDF_PATH, pages=f"{START_PAGE}-{END_PAGE}", guess=False, lattice=True)

    # 4. Concatena todas as tabelas em uma única.
    result = pd.concat(table_list)

    # 5. Chama a função para nomear linhas 
    result = rename_rows(result)

    # 6. Transforma o dataframe em arquivo csv
    print(f"Tabela estruturada criada em {os.path.join(output_path, "csv")}")
    result.to_csv(os.path.join(output_path, "csv", "tabela_estruturada.csv"), index=False)

    # # 7. Compacta o arquivo em zip
    compress_files(os.path.join(output_path, "csv"), "Teste_Yveen.zip", SAVE_ZIP_PATH)

    print("Transformação de Dados finalizado!")