CREATE TABLE IF NOT EXISTS demonstracoes_contabeis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    `data` DATE NOT NULL, 
    reg_ans VARCHAR (255) NOT NULL,
    cd_conta_contabil INT,
    descricao VARCHAR (255),
    vl_saldo_inicial DECIMAL (20,2),
    vl_saldo_final DECIMAL (20,2),
    FOREIGN KEY (reg_ans) REFERENCES relatorio_cadop(registro_ANS)
);
