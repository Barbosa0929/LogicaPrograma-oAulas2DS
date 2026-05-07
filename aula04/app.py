# for 

# laco de for, ele é finito: quando eu sei o numero de repeticoes
#frutas = ['melancia', 'abacaxi', 'melão', 'pera']
#fruta = 'melancia'


    #for in frutas
    # print f 

    #for range(inicio, fim, salto)

    #for _ in range(10+7):
      #  print(i)

'''
num = int(input("Digite um número para saber sua tabuada: "))

for i in range(1,11):
    print(f"{i} X {num} = {i * num}")
    '''

lista_nomes = ['Arthur Cintra de Sousa ', 'João Pedro da Silva', 'Maria Eduarda Souza Lima', 'Lucas Henrique Ferreira Santos', 
'Ana Clara Rodrigues Alves', 'Pedro Gabriel Costa Oliveira', 'Mariana Vitória Pereira Gomes', 'Rafael Augusto Martins Rocha',
'Isabela Cristina Mendes Barros', 'Gustavo Henrique Carvalho Nunes', 'Larissa Beatriz Almeida Lopes', 'Felipe Augusto da Costa',
'Júlia Fernanda Ribeiro Souza', 'Matheus Henrique Alves Lima', 'Amanda Cristina Pereira Santos', 'Gabriel Eduardo Martins Rocha',
'Bianca Vitória Oliveira Gomes', 'Thiago Rafael Carvalho Mendes', 'Beatriz Helena Lopes Ferreira', 'Vinícius Gabriel Nunes Barros',
'Camila Eduarda Almeida Silva', 'Leonardo Henrique Souza Costa', 'Yasmin Cristina Rodrigues Lima', 'Bruno Felipe Pereira Alves',
'Sofia Vitória Mendes Rocha', 'Daniel Augusto Gomes Santos', 'Manuela Beatriz Carvalho Lopes', 'Enzo Gabriel Ferreira Nunes',
'Lara Eduarda Costa Martins', 'Nicolas Henrique Silva Barros', 'Valentina Cristina Souza Almeida']

for i, nome in enumerate(loista_nomes):
    print(f'{i+1}º {nome}')

    nome_buscar = input("Digite um nome para buscar: ").title()

    if nome_buscar in lista_nomes:
        print('usuario encntrado!')