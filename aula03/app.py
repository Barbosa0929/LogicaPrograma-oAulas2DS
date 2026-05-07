

import os

os.system("cls")

print("Boletim escolar")
lista_notas = []
nome = input("Digiteo nome do aluno: ").title()
curso = input("Digite o curso: ").upper()


while True: 
    notas = input("Digite uma nota: ")
    nota = float(nota)
    lista_notas.append(nota)
    print(lista_notas)

    opcao = input("Deseja adicionar mais notas? (S - Sim | n - Não)")
    if opcao == "s":
        continue

    elif opcao == "n":
        break

    media = sum(lista_notas) / len(lista_notas)
   
print(media)