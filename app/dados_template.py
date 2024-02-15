from gerar_estilos import *
from gerar_placemark import *

def dados_template(dados_template, transparencia, espessura):
    template = f'''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>Distribuidores</name>
'''

    cores_set = set()
    for categoria, categoria_data in dados_template.groupby('CATEGORIA'):
        template += f'<Folder><name>{categoria}</name>\n'
        
        for regional, regional_data in categoria_data.groupby('REGIONAL'):
            template += f'<Folder><name>{regional}</name>\n'

            for distribuidor, distribuidor_data in regional_data.groupby('DISTRIBUIDOR'):
                template += f'<Folder><name>{distribuidor}</name>\n'

                for municipio_data in distribuidor_data.itertuples():
                    cor = getattr(municipio_data, 'COR', None)
                    if cor and cor not in cores_set:
                        distribuidor = getattr(municipio_data, 'DISTRIBUIDOR', None)
                        responsavel = getattr(municipio_data, 'RESPONSAVEL', None)
                        endereco = getattr(municipio_data, 'ENDERECO', None)
                        contato_distribuidor = getattr(municipio_data, 'CONTATO2', None)
                        contato_responsavel = getattr(municipio_data, 'CONTATO1', None)
                        populacao = getattr(municipio_data, 'POPULACAO', None)
                        template += gerar_estilos(categoria, cor, transparencia, espessura)
                        cores_set.add(cor)

                    populacao = getattr(municipio_data, 'POPULACAO', None)
                    endereco = getattr(municipio_data, 'ENDERECO', None)
                    contato_distribuidor = getattr(municipio_data, 'CONTATO2', None)
                    contato_responsavel = getattr(municipio_data, 'CONTATO1', None)

                    distribuidor = getattr(municipio_data, 'DISTRIBUIDOR', None)
                    responsavel = getattr(municipio_data, 'RESPONSAVEL', None)
                    municipio_uf = getattr(municipio_data, 'DESCRICAO', None)
                    coordenadas = getattr(municipio_data, 'COORDENADAS', None)

                    cor = getattr(municipio_data, 'COR', None)

                    template += gerar_placemark(contato_responsavel, populacao, distribuidor, responsavel, endereco, municipio_uf, cor, coordenadas, contato_distribuidor)

                template += '</Folder>\n'

            template += '</Folder>\n'

        template += '</Folder>\n'

    template += '''
  </Document>
</kml>
'''
    return template