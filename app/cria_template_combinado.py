from dados_template import *

def cria_template_combinado(df_merged, output_file_path, transparencia, espessura):
    template = dados_template(df_merged, transparencia, espessura)
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(template)