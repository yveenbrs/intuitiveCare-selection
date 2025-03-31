INSERT INTO demonstracoes_contabeis (
    `data`,
    reg_ans,
    cd_conta_contabil,
    descricao,
    vl_saldo_inicial,
    vl_saldo_final
) VALUES (
    %s,
    %s,
    %s,
    %s,
    %s,
    %s
);
