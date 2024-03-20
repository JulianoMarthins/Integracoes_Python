"""
        No código abaixo nós criaremos um novo PDF somente com as páginas 01, 14 e 16

"""

import PyPDF2 as pyf
from pathlib import Path

nome  = "MGLU_ER_3T20_POR.pdf"
arquivo_pdf = pyf.PdfReader(nome)

num_paginas = [1, 14, 16]
novo_arquivo = pyf.PdfWriter()

for num in num_paginas:
    pagina_pdf = pyf.PdfReader(f"Paginas/Arquivo Pagina {num}.pdf")
    novo_arquivo.add_page(pagina_pdf.pages[0])

    with Path (f"Consolidado.pdf").open('wb') as arquivo:
        novo_arquivo.write(arquivo)


