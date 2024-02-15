import pandas as pd
from aplicar_mascara_contato import *

def criar_dataframe_sumarizado(df):
    regional = df['REGIONAL'].tolist()
    razao_social = df['DISTRIBUIDOR'].tolist()
    responsavel = df['RESPONSAVEL'].tolist()
    municipio_uf = df['MUNICIPIO / UF'].tolist()
    populacao = df['POPULACAO'].tolist()
    contato_responsavel = df['CONTATO1'].tolist()
    contato_distribuidor = df['CONTATO2'].tolist()
    endereco = df['ENDERECO'].tolist()

    categorias = []
    for reg in regional:
        categoria = reg.split(' ', 1)[0] if isinstance(reg, str) else ''
        categorias.append(categoria)

    max_length = max(len(regional), len(razao_social), len(responsavel), len(municipio_uf), len(populacao), len(contato_responsavel), len(contato_distribuidor), len(endereco), len(categorias))

    regional.extend([None] * (max_length - len(regional)))
    razao_social.extend([None] * (max_length - len(razao_social)))
    responsavel.extend([None] * (max_length - len(responsavel)))
    municipio_uf.extend([None] * (max_length - len(municipio_uf)))
    populacao.extend([None] * (max_length - len(populacao)))
    contato_responsavel.extend([None] * (max_length - len(contato_responsavel)))
    contato_distribuidor.extend([None] * (max_length - len(contato_distribuidor)))
    endereco.extend([None] * (max_length - len(endereco)))
    categorias.extend([None] * (max_length - len(categorias)))

    summary_df = pd.DataFrame({
        'REGIONAL': regional,
        'DISTRIBUIDOR': razao_social,
        'RESPONSAVEL': responsavel,
        'MUNICIPIO / UF': municipio_uf,
        'POPULACAO': populacao,
        'CONTATO1': contato_responsavel,
        'CONTATO2': contato_distribuidor,
        'ENDERECO': endereco,
        'CATEGORIA': categorias
    })

    summary_df.dropna(subset=['REGIONAL'], inplace=True)
    summary_df['CONTATO1'] = summary_df['CONTATO1'].apply(aplicar_mascara_contato)
    summary_df['CONTATO2'] = summary_df['CONTATO2'].apply(aplicar_mascara_contato)

    unique_razao_social = summary_df['DISTRIBUIDOR'].unique()
    color_mapping = {razao: f"{hash(razao) % 0xffffff:06x}ff" for razao in unique_razao_social}
    summary_df['COR'] = summary_df['DISTRIBUIDOR'].map(color_mapping)

    return summary_df