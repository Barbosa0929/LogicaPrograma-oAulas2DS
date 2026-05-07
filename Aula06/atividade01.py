"""
1.  crie um programa qeu o usuario posso digitar quantos numeros quiser
e ao terminar imprima a lista em ordem crescente

2.  crie um programa que o usuario possa digitar a quantidade desejada de notas
de um determinado aluno (nota minima 0 e nota maxima 10) e o programa calcula 
a media desse aluno, e ao final imprima se o aluno esta (aprovado >=7, reprovado 
recuperação >=5)

"""

2. 

lista_numero = []

while True:
    numero = float(input("Digite um número: "))
    lista_numero.append(numero)
    opcao = input("Deseja adicionar mais? (s - Sim) ou enter para não").lower()
    if opcao != "s":
        break

lista_numero.sort()
print(lista_numero)
