"""
            O objetivo da criação dos arquivos em PDF foi pela necessidade de compartilhar um arquivo que não possa
        ser editador. Porém, isso tem possibilidade de acontecer com Python.

            Possuímos duas bibliotecas em Python com a finalidade de edição e extração de um PDF.

        PyPDF2 -> Esta ferramenta é utilizada para a manupulação geral do PDF, pode ser utilizado para pegar um
    texto específico do pdf, mesclar dois PDF's, adicionar uma página no meio de outras já existentes do arquivo
    original, pode ser movido o sentido das páginas, etc...

        Tabula -> Como o próprio nome já diz, tabula serve para extrair e trabalhar com tabelas existentes nos
    arquivos PDF's, então quando você quiser extrair tabelas e transforma-la em dataframe, o tipo de tabelas
    que o pandas usa, podemos resolver este problema com o Tabula

        A instlaçaõ das bibliotecas devem ser realizadas no terminal com o comando "pip intall pypdf2", como podemos
    observar não há nada demais nesta instalação porém, ao instalar a biblioteca Tabula, devemos ter atenção no modo
    de escrita já que existem duas bibliotecas disponíveis como nomes similares, tabula, e tabula-py. A biblioteca
    que devemos instalar é a segunda opção com o comando "pip intall tabula-py"

        Caso você venha a intalar a biblioteca tabula por necessidade ou sem querer, você precisará configurar algumas
    opções no seu computador porque ambas bibliotecas terião conflitos uma entre elas. Caso você não use a biblioteca 
    tabula você pode desinstalá-la com o comando "pip unistall tabula", depois instalar o tabula-py. Nesta etapa pode 
    ainda, haver conflitos, o que pode ser resolvidos desinstalando o tabula-py e reinstalando a mesma mas assim, resolver
    os conflitos da biblioteca.

         Outra questão ainda sobre o tabula-py, é a necessidade da instalação do java em seu computador, isso porque, tabula
    é uma biblioteca originalmente criada para ter seu funcionamento no java sendo reutilizada no python por sua eficiente
    e qualidade consideravel. Você pode baixar o Java pesquisando "download Java no google, após a instalação, é necessário
    reiniciar o computador. 

"""
import PyPDF2 as pyf
from pathlib import Path

# Salvar página a página do pdf em uma pasta específica

nome = "MGLU_ER_3T20_POR.pdf" # Nome do arquivo a ser lido
arquivo_pdf = pyf.PdfReader(nome) # Armazena na variavel o conteúdo do pdf

for i, pagina in enumerate(arquivo_pdf.pages):
    num_pagina = i + 1
    novo_pdf = pyf.PdfWriter()
    novo_pdf.add_page(pagina)

    with Path(f'Paginas/Arquivo Pagina {num_pagina}.pdf').open(mode='wb') as arquivo:
        novo_pdf.write(arquivo)
