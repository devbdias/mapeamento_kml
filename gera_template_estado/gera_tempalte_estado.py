import xml.etree.ElementTree as ET
import pandas as pd
import os

def ler_arquivo_kml(file_path):
    """Lê um arquivo KML e retorna os dados relevantes."""
    tree = ET.parse(file_path)
    root = tree.getroot()

    df_data = []
    for placemark in root.findall('.//{http://www.opengis.net/kml/2.2}Placemark'):
        name = placemark.find('{http://www.opengis.net/kml/2.2}name').text
        coordenadas = placemark.find('.//{http://www.opengis.net/kml/2.2}coordinates').text
        descricao = placemark.find('.//{http://www.opengis.net/kml/2.2}description').text

        coordenadas = ' '.join(coordenadas.split())

        df_data.append({'Nome': name, 'Coordenadas': coordenadas, 'Descricao': descricao})

    return df_data

def criar_template_kml(estados_data, cor):
    """Cria um template KML a partir dos dados de vários estados."""
    template = f'''
<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>Endereço Distribuidores</name>
    
    <Style id="poly-{cor}-1200-77-nodesc-normal">
      <LineStyle>
        <color>{cor}</color>
        <width>1.2</width>
      </LineStyle>
      <PolyStyle>
        <color>{cor}</color>
        <fill>1</fill>
        <outline>1</outline>
      </PolyStyle>
      <BalloonStyle>
        <text><![CDATA[<h3>$[name]</h3>]]></text>
      </BalloonStyle>
    </Style>

    <Style id="poly-{cor}-1200-77-nodesc-highlight">
      <LineStyle>
        <color>{cor}</color>
        <width>1.8</width>
      </LineStyle>
      <PolyStyle>
        <color>{cor}</color>
        <fill>1</fill>
        <outline>1</outline>
      </PolyStyle>
      <BalloonStyle>
        <text><![CDATA[<h3>$[name]</h3>]]></text>
      </BalloonStyle>
    </Style>

    <StyleMap id="poly-{cor}-1200-77-nodesc">
      <Pair>
        <key>normal</key>
        <styleUrl>#poly-{cor}-1200-77-nodesc-normal</styleUrl>
      </Pair>
      <Pair>
        <key>highlight</key>
        <styleUrl>#poly-{cor}-1200-77-nodesc-highlight</styleUrl>
      </Pair>
    </StyleMap>
'''

    for estado_data in estados_data:
        estado = estado_data['Descricao'].split('/')[0].strip()
        descricao = estado_data['Descricao']
        coordenadas = estado_data['Coordenadas']

        template += f'''
    <Placemark>
      <name>{estado}</name>
      <description>{descricao}</description>
      <styleUrl>#poly-{cor}-1200-77-nodesc</styleUrl>
      <Polygon>
        <outerBoundaryIs>
          <LinearRing>
            <tessellate>1</tessellate>
            <coordinates>
              {coordenadas}
            </coordinates>
          </LinearRing>
        </outerBoundaryIs>
      </Polygon>
    </Placemark>
'''

    template += '''
  </Document>
</kml>
'''
    return template


def processar_arquivos_kml(diretorio, cor):
    """Processa todos os arquivos KML no diretório."""
    df_data = []

    for file_name in os.listdir(diretorio):
        if file_name.endswith('.kml'):
            file_path = os.path.join(diretorio, file_name)
            dados = ler_arquivo_kml(file_path)
            df_data.extend(dados)

    output_file_path = fr'C:\Users\bruno\OneDrive\Área de Trabalho\Fluxo de trabalho\mapeamento\saida\estados.kml'

    template = criar_template_kml(df_data, cor)

    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(template)

    print(fr"Template salvo com sucesso no arquivo {output_file_path}")

    return df_data

def main():
    """Função principal."""
    dir_path = r'C:\Users\bruno\OneDrive\Área de Trabalho\Fluxo de trabalho\mapeamento\kml-brasil-master\lib\2010\estados\kml'
    cor = 'ba20aaff'

    df_coordinates = pd.DataFrame(processar_arquivos_kml(dir_path, cor))

    df_coordinates[['Estado', 'Regiao']] = df_coordinates['Descricao'].str.split('/', n=1, expand=True)

    print(df_coordinates)

if __name__ == "__main__":
    main()
