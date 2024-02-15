import pandas as pd
import os
from ler_arquivos_kml import *

def processar_arquivos_kml(diretorio):
    """Processa todos os arquivos KML no diretório e retorna um DataFrame."""
    df_data = []
    
    for estado in os.listdir(diretorio):
        estado_path = os.path.join(diretorio, estado)

        for tipo in os.listdir(estado_path):
            tipo_path = os.path.join(estado_path, tipo)
            
            if 'kml' in tipo and os.path.isdir(tipo_path):
                for file_name in os.listdir(tipo_path):
                    if file_name.endswith('.kml'):
                        file_path = os.path.join(tipo_path, file_name)
                        dados = ler_arquivo_kml(file_path)
                        df_data.extend(dados)
    return df_data