"""
        Vimos em aulas passadas que existem três modos de abrir um arquivo em Python pelo método open, passando a string no
    argumento para definir a ação que teremos com este arquivo, sendo ele o modo de leitura, de escrita ou de adição de conteúdo.

        Mas qual a diferença entre escrever e adicionar uma informação do arquivo?

        Quando abrimos um arquivo em modo de escrita, o Python irá escrever e salvar tudo o que ordenarmos no arquivo porém, caso
    exista algo salvo neste arquivo, o python sobreescreverá as informações do algoritmo sobre o arquivo original ocasionando a
    perca das informações passadas.
        Já o modo de adicinoar elementos ao arquivo, apenas acrescentará as informações passadas por nós no algoritmo e salvará
    essas informações sem perder os dados antigos contidos nesse documento.

"""


# O código abaixo irá criar um arquivo em modo de escrita. 
arquivo = open('Resumo.txt', 'w')

# O código abaixo irá escrever o texto, porém, ao contrário do que o professor afirmou durante a aula, este arquivo é salvo no
# diretório do projeto salvando as informações escritas no argumento do metodo. 
arquivo.write('Olá, meu nome é Juliano\n')

# No código abaixo acrescentaremos mais uma informação, o código \n, quebra de linha, deve estar no código caso você deseje
# que a nova escrita esteja em uma nova linha.
arquivo.write('Sou estudante de Python\n')

arquivo.write('Estou formado em análise e desenvolvimento de sistemas\n')
arquivo.write('Neste corrente ano desejo migrar para área de programação.\n')
arquivo.write('Boa sorte a todos nós.\n')

# Seguindo a aula, o método abaixo deverá fechar o arquivo e salvar as alterações realizadas até então
arquivo.close()

# Segundo o professor todos os metodos que forem de abertura de algum tipo de arquivo, deverá ser encerrado posteriormente para 
# seu perfeito funcionamento, exatamente como o scan do Java.

