import PyPDF2 as pyf
from pathlib import Path

arquivo = pyf.PdfReader("MGLU_ER_3T20_POR.pdf") # Armazena na variavel o arquivo em pdf

quantidade_paginas = len(arquivo.pages) # Retorna a quantidade de páginas do pdf
metados_arquivo = arquivo.metadata # Retorna um dicionários com as informações gerais do arquivo


print(f'\nQuantidade de páginas do PDF: {quantidade_paginas}')

# print(f'\nInformações sobre o PDF: \n{metados_arquivo }')


# Extrair um texto específico da alguma página do pdf.

print('\n')

texto_referencia = "| Despesas com Vendas"

for num, pagina in enumerate(arquivo.pages):
    texto_pagina = pagina.extract_text()
    if texto_referencia in texto_pagina:
        texto_analisar = texto_pagina
        print(f'Número da página com texto referêcnia: {num + 1}')
        break

print()
posicao_inicial = texto_analisar.find(texto_referencia)
posicao_final = texto_analisar.find("|", posicao_inicial + 1)
texto_final = texto_analisar[posicao_inicial: posicao_final]

print(texto_final)