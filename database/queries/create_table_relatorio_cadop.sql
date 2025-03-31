CREATE TABLE IF NOT EXISTS relatorio_cadop (
    registro_ANS VARCHAR (255) NOT NULL PRIMARY KEY,
    cnpj VARCHAR (255) NOT NULL,
    razao_social VARCHAR (255) NOT NULL,
    nome_fantasia VARCHAR (255),
    modalidade VARCHAR (255) NOT NULL,
    logradouro VARCHAR (255) NOT NULL,
    numero VARCHAR (255) NOT NULL,
    complemento VARCHAR (255),
    bairro VARCHAR (255) NOT NULL,
    cidade VARCHAR (255) NOT NULL,
    uf VARCHAR (255) NOT NULL,
    cep VARCHAR (255) NOT NULL,
    ddd VARCHAR (255),
    telefone VARCHAR (255),
    fax VARCHAR (255),
    endereco_eletronico VARCHAR (255),
    representante VARCHAR (255) NOT NULL,
    cargo_representante VARCHAR (255) NOT NULL,
    regiao_de_comercializacao INT,
    data_registro_ans DATE NOT NULL
);


