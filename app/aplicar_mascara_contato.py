import pandas as pd
import re

def aplicar_mascara_contato(contato):
    if pd.notna(contato):
        contato_numerico = re.sub(r'[^\d.]', '', str(contato))
        
        if re.match(r'\d+(\.\d+)?$', contato_numerico):
            contato_numerico = re.sub(r'(\d{2})(\d{4,})(\d{4})', r'\1 \2-\3', contato_numerico)
            contato_string = str(contato_numerico)
            return contato_string[:-2]
    return ''