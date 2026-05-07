'''
Programa  01 - Aula04 - 28/04
Prof: Karython
Turma: 2DS

sistema de sorteios 
'''

import os 
import random

lista_nomes =  ['Arthur Cintra de Sousa ', 'João Pedro da Silva', 'Maria Eduarda Souza Lima', 'Lucas Henrique Ferreira Santos', 
'Ana Clara Rodrigues Alves', 'Pedro Gabriel Costa Oliveira', 'Mariana Vitória Pereira Gomes', 'Rafael Augusto Martins Rocha',
'Isabela Cristina Mendes Barros', 'Gustavo Henrique Carvalho Nunes', 'Larissa Beatriz Almeida Lopes', 'Felipe Augusto da Costa',
'Júlia Fernanda Ribeiro Souza', 'Matheus Henrique Alves Lima', 'Amanda Cristina Pereira Santos', 'Gabriel Eduardo Martins Rocha',
'Bianca Vitória Oliveira Gomes', 'Thiago Rafael Carvalho Mendes', 'Beatriz Helena Lopes Ferreira', 'Vinícius Gabriel Nunes Barros',
'Camila Eduarda Almeida Silva', 'Leonardo Henrique Souza Costa', 'Yasmin Cristina Rodrigues Lima', 'Bruno Felipe Pereira Alves',
'Sofia Vitória Mendes Rocha', 'Daniel Augusto Gomes Santos', 'Manuela Beatriz Carvalho Lopes', 'Enzo Gabriel Ferreira Nunes',
'Lara Eduarda Costa Martins', 'Nicolas Henrique Silva Barros', 'Valentina Cristina Souza Almeida']

lista_sorteados = []
sorteados = 0
while sorteados < 5:
    nome_sorteado = random.choice(lista_nomes)
    print(f'sorteado: {nome_sorteado}')
    lista_sorteados.append(nome_sorteado)

    print(f'Lista antes de remover {len(lista_nomes)}')

    lista_nomes.remove(nome_sorteado)

    print(f'Lista atualizada {len(lista_nomes)}')

    sorteados +=1

    print('Fim do programa')

