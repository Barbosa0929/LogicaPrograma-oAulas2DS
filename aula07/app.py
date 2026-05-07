"""
    Manipulação de arquivos: percorrer os meus diretorios,encontrar arquivo
    passar o comando de abertura de arquivo, passar comando de ação.

    arquivo = open('arquivo.txt', 'modo')

    modos de ação:
        - "r" : leitura do arquivo
        - "w" : escrita(sobescreve o conteudo antigo)
        - "a" : adciona conteudo
        - "x" : criar arquivo
        - "b" : arquivos binarios
        - "t" : texto
"""

# criando e escrevendo arquivo
arquivo = open('Primeiro_arquivo.txt', "w")
arquivo.write('Olá mundo! meu primeiro arquivo')
arquivo.close()

# lwndo arquivo
arquivo = open("primeiro_arquivo.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

# aplicando boa pratica
with open("Primeiro_arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# arquivos com multiplas escritas 
with open('alunos.txt', "w") as arquivo:
    arquivo.write('Ana\n')
    arquivo.write('Joao\n')
    arquivo.write('gomes\n')
    arquivo.write('pedro\n')
    arquivo.write('tanaka\n')
    arquivo.write('jeronimo\n')
    arquivo.write('davi\n')

# lendo linha a linha
with open('alunos.txt', "r") as arquivo:
    for linha in arquivo:
        print(linha)

# usando lista para escrever arquivo
frutas = ['pera', 'abacaxi', 'melancia', 'manga', 'caju', 'morango']

with open('frutas.txt', "w") as arquivo:
    for f in frutas:
        arquivo.write(f + '\n') 

# converten o arquivo em uma lista
with open('frutas.txt', "r") as arquivo:
    linhas = arquivo.readlines()

print(type(linhas))
print(linhas) 

# saida: ['pera', 'abacaxi', 'melancia', 'manga', 'caju', 'morango']

# limpar a quebra de linha 

with open('frutas.txt', "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())

# exemplo para cadastro

while True:
    nome = input("Digite seu nome: ").title()

    with open("cadastro.txt", 'a') as arquivo:
        arquivo.write(nome + "\n")

    sair = input("Deseja sair? s/n").lower()

    if sair == 's':
        break


        