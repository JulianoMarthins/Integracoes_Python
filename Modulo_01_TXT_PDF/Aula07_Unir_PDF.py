import PyPDF2 as pyf
from pathlib import Path

pdf_mesclado = pyf.PdfMerger()

pdf_mesclado.append("MGLU_ER_3T20_POR.pdf")
pdf_mesclado.append("MGLU_ER_4T20_POR.pdf")

with Path("Mesclado.pdf").open("wb") as arquivo:
    pdf_mesclado.write(arquivo)

