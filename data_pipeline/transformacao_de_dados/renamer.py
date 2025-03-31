
def rename_rows(result):
    """
    Função para localizar as linhas que possuem OD e AMD e substitui-las dentro do dataframe,
    além das colunas.
    """
    output = result.copy()
    output.loc[output["OD"].notna(), "OD"] = "Seg. Odontológica"
    output.loc[output["AMB"].notna(), "AMB"] = "Seg. Ambulatorial"
    
    output.rename(columns={"OD": "Seg. Odontológica"}, inplace=True)
    output.rename(columns={"AMB": "Seg. Ambulatorial"}, inplace=True)

    return output