"""
desenvolva um sistema que receba do usuario
seu nome, data de nascimento, peso e altura.
formate a saida para aparecer na tela do usuario:
Olá {nome_informado}, seja bem vindo ao sistema Python 
aqui estão suas informações 
data de nascimenton:
altura:
peso:
"""

nome = str(input("Digite seu nome: "))
dataNasc = str(input("Digite sua data de nascimento completa: "))
altura = float(input("Digite sua altura:"))
peso = float(input("Digite seu peso: "))

print("Olá", nome, "Seja bem vindo ao sistema Python, aqui estão as suas informações")
print("Você nasceu na data: ", dataNasc)
print("Sua altura é: ", altura)
print("Seu peso é: ", peso)

print(type(nome))
