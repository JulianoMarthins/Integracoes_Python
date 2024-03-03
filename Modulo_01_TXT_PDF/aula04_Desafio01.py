"""
        Na Hashtag, sempre analisamos o nosso "funil de vendas". Para isso, rastreamos de onde veio os aluinos
    por meio de um código.

        hashtag_site_org => Pessoas que vieram pelo site da hashtag
        hastag_yt_org => Pessoas que vieram pelo site do youtube
        hastag_ig_org => Pessoas que vieram pelo Instagram da hastag
        hastag_igfb_org => Pessoas que vieram pelo instagram ou facebook da hastag

    Os códigos diferentes disso, são códigos de anúncio da Hashtag

        Queremos analisar quantos alunos vieram de anúncios e quantos vieram organigamente a hastag
        Qual a melhor fonte organica de alunos

    Obs: Organico é tudo aquilo que não veio de anúncios

    Nosso ssitema, consegue exportar um arquivo txt com as informações dos alunos, conforme o arquivo Alunos.txt.

"""
print()
arquivo = open('Alunos.txt', 'r')

# readline lê linha a linha enquanto o readlines criar uma lista para cada linha contida no arquivo
linhas = arquivo.readlines()

# Exclui as três primeiras linhas da lista, as mesmas não tem importância para nosso análise
del linhas[:4]

# Criar os indicadores
rede_social = 0
organico = 0
youtube  = 0
anuncio = 0
site = 0

# Analisando o arquivo e realizando as contagens dos indicadores
for linha in linhas:
    email, origem = linha.split(',')
        
    if '_org' in origem:
        organico += 1

        if 'hashtag_site' in origem:
            site += 1
        if 'hashtag_yt' in origem:
            youtube += 1
        if 'hashtag_ig' in origem or 'igfb' in origem:
            rede_social += 1

    else:
        anuncio += 1

# Salvar os indicadores em um arquvo .txt
escrita = open('Indicadores do site.txt', 'w')

escrita.write('Análise dos indicadores dos alunso da HashTag Treinamentos\n\n')
escrita.write(f'Origem das assinaturas dos alunos da HashTag Treinamentos\nMarketing: {anuncio}\nOrganicos: {organico}\n')

escrita.write('\nOs alunos organicos encontraram a HashTag Treinamentos via:\n')
escrita.write(f'Site HashTag Treinamentos: {site}\nRedes Sociais: {rede_social}\nYouTube: {youtube}\n')

escrita.write(f'\nTotal de Alunos: {anuncio + organico}')

arquivo.close()
escrita.close()