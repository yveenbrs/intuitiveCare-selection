# intuitiveCare_selection
Este repositório contém as respostas para o teste de nivelamento realizado pela Intuitve Care.
Ele está organizado com pastas específicas para cada parte do teste.

# Estrutura
/data_pipelane: Contém os arquivos necessários para Web Scraping e a Transformação de dados (questões 1 e 2).
  /output: Armazena os arquivos salvos pelo Web Scraping.
  /webscraping: Executando o arquivos web_scraping.py, realiza a leitura html, salvando todos os arquivos na pasta output.
    required: import requests, BeautifulSoup
  /transformacao_de_dados: Executando o arquivos transformacao_de_dados.py, realiza a transformação dos dados do PDF Anexo 1.
    required: import pandas, tabula, os
  /utils: Armazena o arquivo functions.py necessário para funcionar a compilação de arquivos.
    required: import zipfila, os
/database: Contém os arquivos para manipulação de banco de dados (questão 3).
  main.py: Executa todas as queries.
    required: Banco de dados Mysql / import mysql.connector, os
  utils.py: Armazena todas as funções usadas na main.py.
  required: import mysql.connector, os, pandas, re
  /queries: Armazena todos os sqls solicitados na questão de create, insert e select. 
  /cvs: Armazena o arquivo csv usado.
/api_Vue: Contém os arquivos para funcionamento de uma API em Python e front em Vue.js (questão 4).
  app.py: Arquivo que possui a API.
    required: Executar: "python app.py" no terminal
  utils.py: Amazena os métodos usados.
    required: import csv
  /cadop-app: Possui todo o funcionamento do frontend usando Vue.js
    required: Vue.js installed / Executar: "npm run serve" no terminal da pasta
  /csv: Armazena o arquivo solicitado para uso.
