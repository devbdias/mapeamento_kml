import pandas as pd
from criar_dataframe_sumarizado import *
from processar_arquivos_kml import *

def merge_arquivos(data_frame, diretorio):
    df_distribuidores = criar_dataframe_sumarizado(data_frame)
    df_municipios_data = processar_arquivos_kml(diretorio)
    
    df_municipios = pd.DataFrame(df_municipios_data)

    df_distribuidores.dropna(subset=['MUNICIPIO / UF'], inplace=True)

    df_merged = pd.merge(df_distribuidores, df_municipios, how='left', left_on='MUNICIPIO / UF', right_on='DESCRICAO')

    return df_merged