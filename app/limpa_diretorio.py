import os

def limpa_diretorio(diretorio):
    try:
        if os.path.exists(diretorio):
            arquivos = os.listdir(diretorio)

            for arquivo in arquivos:
                caminho_completo = os.path.join(diretorio, arquivo)
                if os.path.isfile(caminho_completo):
                    os.remove(caminho_completo)
                elif os.path.isdir(caminho_completo):
                    os.rmdir(caminho_completo)
    except Exception as e:
        print(f"Ocorreu um erro durante a limpeza do diretório: {e}")