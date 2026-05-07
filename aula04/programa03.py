"""
sistema: calculadora

"""

while True:
    print(30*"-", "calculadora",30*"-")
    num1 = int(input('Digite um numero: '))
    num2 = int(input('Digite o segundo numero: '))

    print('1. Soma')
    print('2. Subtracão')
    print('3. Multiplicacão')
    print('4. Divisão')
    opcão = input('Digite a operação: ')

    match opcão:
        case '1':
            resultado = num1 + num2
            print(f'{num1} + {num2} = {resultado}')
            break
        case '2':
            resultado = num1 - num2
            print(f'{num1} - {num2} = {resultado}')
            break
        case '3':
            resultado = num1 * num2
            print(f'{num1} * {num2} = {resultado}')
            break
        case '4':
            if num1 != 0 and num2 != 0:
                resultado = num1 / num2
                print(f'{num1} / {num2} = {resultado}')
            break
       
        case _:
            print("Digite um numero válido")