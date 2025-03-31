import os

from .downloader import download_pdf
from .scraper import get_html, localize_files
from utils.functions import compress_files

def main(output_path):
    # 1. Define as variáveis de ambiente.
    URL = (
        "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    )
    SAVE_PDF_PATH = os.path.join(output_path, "pdf")
    SAVE_ZIP_PATH = os.path.join(output_path, "zip")

    # 2. Obtem o html do endereço informado.
    html = get_html(URL)
    # 3. Localiza os links href no html que possuem a nomeclatura Anexo.
    pdf_files_url = localize_files(html)

    # 4. Caso localize usa o método download_pdf para salvar os links encontrados em PDF. 
    if pdf_files_url:
        for index, link in enumerate(pdf_files_url):
            save_path = os.path.join(SAVE_PDF_PATH, "Anexo " + str(index + 1) + ".pdf")
            download_pdf(save_path, link)
    else:
        print("Nenhum link solicitado foi encontrado no html fornecido.")

    # 5. Comprime os arquivos anteriormente salvos em PDF.
    compress_files(SAVE_PDF_PATH, "anexos_compactados.zip", SAVE_ZIP_PATH)

    print("Web scraping finalizado!")