import pandas as pd
import xml.etree.ElementTree as ET
import warnings

from limpa_diretorio import *
from merge_arquivos import*
from cria_template_combinado import *

warnings.filterwarnings("ignore", category=FutureWarning)


def main():
    
    transparencia = 0.8
    espessura = 0.2

    caminho_arquivo = r'C:\Users\bruno\OneDrive\Área de Trabalho\Fluxo de trabalho\mapeamento\excel\BRUNO.xlsx'    
    output_file_path = r'C:\Users\bruno\OneDrive\Área de Trabalho\Fluxo de trabalho\mapeamento\saida\distribuidores_kml\unificado\distribuidores.kml'
    diretorio_a_limpar = r'C:\Users\bruno\OneDrive\Área de Trabalho\Fluxo de trabalho\mapeamento\saida\distribuidores_kml\unificado'
    diretorio_kml = r'C:\Users\bruno\OneDrive\Área de Trabalho\Fluxo de trabalho\mapeamento\kml-brasil-master\lib\2010\municipios'

    limpa_diretorio(diretorio_a_limpar)

    df = pd.read_excel(caminho_arquivo, sheet_name='BASE LIMPA')

    df_result = merge_arquivos(df, diretorio_kml)    
    cria_template_combinado(df_result, output_file_path, transparencia, espessura)

if __name__ == "__main__":
    main()
