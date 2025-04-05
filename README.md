# Intuitive Care - Nivelamento

Soluções para o teste de nivelamento aplicado pela **Intuitive Care**, estruturadas em diretórios correspondentes a cada seção do desafio. A organização visa garantir clareza na separação de etapas e facilitar a revisão do código-fonte e da lógica aplicada em cada parte.

---

## Estrutura do Projeto

- **data_pipelane**: Contém os arquivos necessários para Web Scraping e a Transformação de dados (questões 1 e 2)
- **database:** Contém os arquivos para manipulação de banco de dados (questão 3).
- **api_Vue:** Contém os arquivos para funcionamento de uma API em Python e front em Vue.js (questão 4).


### Data Pipelane:
- **main.py:** Arquivo main responsável por acionar os métodos de web scraping e transformação de dados em ordem.  
- **/output:** Armazena os arquivos salvos pelo Web Scraping.  
- **/webscraping:** Contém os arquivos necessários para todo o processo de Web Scraping, realizando a leitura html, salvando todos os arquivos na pasta output.  
`"requer: import requests, BeautifulSoup, os"`  
- **/transformacao_de_dados:** Contém os arquivos responsáveis por realizar a transformação dos dados do PDF Anexo 1.  
`"requer: import pandas, tabula, os"`   
- **/utils:** Armazena o arquivo functions.py necessário para funcionar a compilação de arquivos.
`"requer: import zipfila, os"`  


### Database:
- **main.py:** Executa todas as queries SQL.
`"requer: Banco de dados Mysql / import mysql.connector, os"`
- **/utils:** Armazena todas as funções usadas na main.py.
`"requer: import mysql.connector, os, pandas, re"` 
- **/queries:** Armazena todos os sqls solicitados na questão de create, insert e select.  
- **/cvs:** Armazena o arquivo csv usado.


### API Vue.js:
- **app.py:** Arquivo que possui a API em Flask responsável por leitura do arquivo CSV e retorno em json.
`"execução: Executar: "python app.py" no terminal"`
- **utils.py:** Amazena os métodos usados como a leitura de CSV.
`"requer: import csv"`
- **/cadop-app:** Armazena todos os arquivos/componentes do Vue.js.
`"requer: Vue.js installed / Executar: "npm run serve" no terminal da pasta"`
- **/csv:** Armazena o arquivo solicitado para uso.  
