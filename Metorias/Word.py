# Importação do modulo de integração do Python com o Word
from docx import Document



# Criando o documento no Python
documento = Document()


# Aqui editamos o texto

faturamento = 1000

texto = f"""
        Estamos realizando as configurações iniciais para a integração
    do Python com o word.

        O faturamento da empresa no dia 04 de março de 2024 foi de R$ {faturamento}

"""

paragrafo = documento.add_paragraph(texto)

# Importação dos modulos de formatação do Word
# 'pt' -> permitira a formatação do tamanho da fonte
# 'RGBColor' -> permitirá a formatação das cores da fonte
# 'Cm' -> permitirá formatar o tamanho das margens da página, cm vem de centimetros
# 'WD_BUILTIN_STYLE' -> Permite criar um estilo de formatação próprio.
from docx.shared import Pt, RGBColor, Cm 
from docx.enum.style import WD_STYLE_TYPE

# paragrafo.style = documento.style.add_style("EstiloLira", WD_STYLE_TYPE.PARAGRAPH)
paragrafo.style.font.name = 'Algerian'
paragrafo.style.font.size = Pt(15)
paragrafo.style.font.italic = True


# Salvar o documento no computador 
documento.save('Documento.docx')