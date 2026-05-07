"""
1.  crie um programa qeu o usuario posso digitar quantos numeros quiser
e ao terminar imprima a lista em ordem crescente

2.  crie um programa que o usuario possa digitar a quantidade desejada de notas
de um determinado aluno (nota minima 0 e nota maxima 10) e o programa calcula 
a media desse aluno, e ao final imprima se o aluno esta (aprovado >=7, reprovado 
recuperação >=5)
"""
2.

import os

print("Boletim escolar ")

lista_notas = []
nome = input("Digite o nome do aluno: ").title()
curso = input("Digite o curso: ").upper()

while True: 
 nota= input("Digite uma nota: ")
 nota = float(nota)
 lista_notas.append(nota)
 print(lista_notas)
  
 opcao = input("Deseja adicionar mais notas? (Enter - continue | n- Não)").lower()
 if opcao == "n": 
   break

media = sum(lista_notas) / len(lista_notas)
print(f'{media:.2}')

if media >= 7: 

    resultado = "Aprovado" 

elif media >= 5: 

    resultado = "Recuperação" 
else:
    resultado = "Reprovado"

print(resultado)
