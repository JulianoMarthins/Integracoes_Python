"""
                        Integração do Python com arquivos .txt

        Como quase tudo em Python, existem várias formas de ler um arquivo.

        Aprendemos em módulos passados a ler arquivos em Excel ou .csv com a biblioteca 
        Pandas, a recomendação é que, sempre
    que necessário ler arquivos no Python, utilizar o pandas para realizar este processo 
    porque ele é um módulo feito para
    análise de dados, e nele, já tem muitas funcões e métodos prontos que nos ajudaram no 
    uso dos dados desses arquivos.

    Caso você queira ler um arquivo .txt simplesmente, ou escrever um, vamos agora, ver 
    como podemos fazer isso no Python

        Estrutura 01 -> Existe nativamente no Python um método chamado open, que serve para abrir o arquivo passado como parâmetro, 
    exemplo:

        arquivo = open('Nome_arquivo', 'r')

        Análisando o código acima, observamos que existem dois parâmetros passado como argumento ao método, o nome do arquivo
    que, deve estar no mesmo diretório do algoritmo ou, ao invés da utilização do nome do arquivo, antes deste, deve ser digitado
    todo o caminho do arquivo em questão. 

        O segundo parâmetro é a string "r", o que significa a ação que tomaremos ao utilizar a variavel arquivo, ao todo são três
    caracteres que podem ser passado como argumento de ação, (r, w, a), que representam

        r -> read, abriremos o arquivo em modo de leitura
        w -> write, abriremos o arquivo em modo de escrita
        a -> append, podemore adicionar informações ao arquivo aberto.

    
"""
# O código abaixo abre o arquivo Alunos.txt em modo de leitura
arquivo = open('Alunos.txt', 'r')

"""
        Para imprimir as informações contidas na variável arquivo, existem dois métodos no python para executar esta tarefa, o métido
    read() e o método readlines(), ambos realização a tarefa com suas particulariedades

        O método read() imprimirá as informações do arquivo como se fosse um texto, exatamente igual como está originalmente no arquivo
    lido.
        O método readlines() se torna mais interessante porque ele transforma o arquivo em uma lista em python onde cada linha do arquivo
    será um item dessa lista, sendo assim, pode ser utilizado todos os métodos que aprendemos nos capitulos em que trabalhamos com listas.
"""
print()

# O código abaixo imprime o conteúdo armazenado na variavel arquivo como um arquivo de texto
#print(f'Abrindo o arquivo pelo método .read():\n\n{arquivo.read()}')

# O código abaixo imprime o conteúdo armazenado na variavel convertida pra listas
print(f'\n\nAbrindo o arquivo pelo método .readlines():\n\n {arquivo.readlines()}')





