"""
                        Integração do Python com arquivos .txt

        Como quase tudo em Python, existem várias formas de ler um arquivo.

        Aprendemos em módulos passados a ler arquivos em Excel ou .csv com a biblioteca Pandas, a recomendação é que, sempre
    que necessário ler arquivos no Python, utilizar o pandas para realizar este processo porque ele é um módulo feito para
    análise de dados, e nele, já tem muitas funcões e métodos prontos que nos ajudaram no uso dos dados desses arquivos.

    Caso você queira ler um arquivo .txt simplesmente, ou escrever um, vamos agora, ver como podemos fazer isso no Python


"""

# Estrutura 01 - Existe nativamente no Python um método chamado < arquivo = open("NomeArquivo", 'r')> , analisando o código,
# podemos observar que uma variável recebe o conteúdo que será aberto pelo método open, em seu argumento, passa o nome do arquivo
# que se deseja abrir e com segundo argunto, um caracter que define o que será realizado neste arquivo, por exemplo, se ao abrir
# o arquivo, a finalidade seja somente ler o arquivo, deve passar o 'r', que significa read, ou em sua tradução, ler,conforme 
# exemplo acima, caso voce deseje abrir o arquivo e escrever algo neste, você deveria usar o caracter 'w' de write, ou em sua
# tradução, escrever, caso você pretenda adicinoar elementos ao arquivo, deve ser pasado o caracter 'a', de append, como parâmetro


arquivo = open('Alunos.txt', 'r') # Aberto o arquivo 'alunos.txt' em modo de leitura

print(arquivo.read())

