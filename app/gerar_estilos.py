def gerar_estilos(categoria, cor, transparencia, espessura):
    if categoria == '':
        cor = 'FFFFFF'
    else:
        cor = cor

    return f'''
    <Style id="poly-{cor}-1200-77-nodesc-normal">
      <LineStyle>
        <color>FFFFFFFF</color>
        <width>{espessura}</width>
      </LineStyle>
      <PolyStyle>
        <color>{cor}</color>
        <fill>1</fill>
        <outline>1</outline>
      </PolyStyle>
    </Style>
    <Style id="poly-{cor}-1200-77-nodesc-highlight">
      <LineStyle>
        <color>FFFFFFFF</color>
        <width>{transparencia}</width>
      </LineStyle>
      <PolyStyle>
        <color>{cor}</color>
        <fill>1</fill>
        <outline>1</outline>
      </PolyStyle>
    </Style>
    <StyleMap id="poly-{cor}-1200-77-nodesc">
      <Pair>
        <key>normal</key>
        <styleUrl>#poly-{cor}-1200-77-nodesc-normal</styleUrl>
      </Pair>
      <Pair>
        <key>highlight</key>
        <styleUrl>#poly-FFFFFFFF-1200-77-nodesc-highlight</styleUrl>
      </Pair>
    </StyleMap>
'''