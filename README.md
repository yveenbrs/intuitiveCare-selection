# intuitiveCare_selection
Este repositório contém as respostas para o teste de nivelamento realizado pela Intuitive Care.  
Ele está organizado com pastas específicas para cada parte do teste.

## Estrutura
1. **/data_pipelane:** Contém os arquivos necessários para Web Scraping e a Transformação de dados (questões 1 e 2).  
_main.py: Arquivo main responsável por acionar os métodos de web scraping e transformação de dados em ordem.  
_/output: Armazena os arquivos salvos pelo Web Scraping.  
_/webscraping: Contém os arquivos necessários para todo o processo de Web Scraping, realizando a leitura html, salvando todos os arquivos na pasta output.  
required: import requests, BeautifulSoup,os  
_/transformacao_de_dados: Contém os arquivos responsáveis por realizar a transformação dos dados do PDF Anexo 1.  
required: import pandas, tabula, os  
_/utils: Armazena o arquivo functions.py necessário para funcionar a compilação de arquivos.  
required: import zipfila, os  
  
2. **/database:** Contém os arquivos para manipulação de banco de dados (questão 3).  
_main.py: Executa todas as queries.  
required: Banco de dados Mysql / import mysql.connector, os  
_utils.py: Armazena todas as funções usadas na main.py.  
required: import mysql.connector, os, pandas, re  
_/queries: Armazena todos os sqls solicitados na questão de create, insert e select.  
_/cvs: Armazena o arquivo csv usado.  
  
3. **/api_Vue:** Contém os arquivos para funcionamento de uma API em Python e front em Vue.js (questão 4).  
_app.py: Arquivo que possui a API.  
required: Executar: "python app.py" no terminal  
_utils.py: Amazena os métodos usados.  
required: import csv  
_/cadop-app: Possui todo o funcionamento do frontend usando Vue.js  
required: Vue.js installed / Executar: "npm run serve" no terminal da pasta  
_/csv: Armazena o arquivo solicitado para uso.  
