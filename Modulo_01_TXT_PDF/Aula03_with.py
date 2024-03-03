
# O código abaixo funciona como um bloco de código que executa os algoritmos a eles identados, isso significa que o proprio
# Python abrirá o arquivo e o fechará ao final da estrutuda with

with open('Resumo2.txt', 'w') as arquivo:
    arquivo.write('Teste de escrita\n')
    arquivo.write('Com o uso do with\n')

print('\nFim do código')