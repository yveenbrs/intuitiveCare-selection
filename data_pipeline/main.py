import os

from web_scraping import web_scraping
from transformacao_de_dados import transformacao_de_dados

if __name__ == "__main__":
    web_scraping.main(os.path.join(os.getcwd(), "output"))
    transformacao_de_dados.main(os.path.join(os.getcwd(), "output"))
    