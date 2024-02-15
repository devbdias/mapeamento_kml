def gerar_placemark(contato_responsavel, populacao, distribuidor, responsavel, endereco, municipio_uf, cor, coordenadas, contato_distribuidor):
    return f'''
    <Placemark>
      <name>
          {municipio_uf}\nPOPULAÇÃO: {populacao}
      </name>
      <description>
          DISTRIBUIDOR: {distribuidor}\nCONTATO DISTRIBUIDOR: {contato_distribuidor}\nRESPONSÁVEL: {responsavel.upper()}\nCONTATO RESPONSÁVEL: {contato_responsavel}\nENDEREÇO: {endereco} 
      </description>
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