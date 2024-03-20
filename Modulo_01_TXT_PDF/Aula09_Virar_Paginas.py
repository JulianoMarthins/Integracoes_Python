import PyPDF2 as pyf
from pathlib import Path

arquivo_original = pyf.PdfReader("MGLU_ER_3T20_POR.pdf")

novo_arquivo = pyf.PdfWriter()

for pagina in arquivo_original.pages:
    pagina.rotate(90)
    novo_arquivo.add_page(pagina)

with Path('Pagina Rotacionadas.pdf').open('wb') as arquivo:
    novo_arquivo.write(arquivo)

