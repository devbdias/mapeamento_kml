import xml.etree.ElementTree as ET

def ler_arquivo_kml(file_path):
    """Lê arquivos KML em um diretório e retorna os dados relevantes."""
    df_data = []
    tree = ET.parse(file_path)
    root = tree.getroot()

    for placemark in root.findall('.//{http://www.opengis.net/kml/2.2}Placemark'):
        name = placemark.find('{http://www.opengis.net/kml/2.2}name').text
        coordenadas = placemark.find('.//{http://www.opengis.net/kml/2.2}coordinates').text
        descricao = placemark.find('.//{http://www.opengis.net/kml/2.2}description').text
        coordenadas = ' '.join(coordenadas.split())

        df_data.append({'MUNICIPIO': name, 'DESCRICAO': descricao, 'COORDENADAS': coordenadas })
    return df_data
