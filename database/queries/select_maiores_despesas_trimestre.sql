SELECT rc.razao_social, SUM(dc.vl_saldo_final - dc.vl_saldo_inicial) AS total_despesas
    FROM demonstracoes_contabeis dc
    JOIN relatorio_cadop rc ON dc.reg_ans = rc.registro_ANS
    WHERE dc.descricao LIKE '%EVENTOS%'
    AND dc.descricao LIKE '%SINISTROS%'
    AND dc.descricao LIKE '%MEDICO HOSPITALAR%'
    AND dc.data = '2024-10-01'
    GROUP BY rc.razao_social
    ORDER BY total_despesas DESC
    LIMIT 10;
