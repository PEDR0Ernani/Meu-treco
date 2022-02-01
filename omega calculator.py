import math
quant = opcao = 0

while True:
    valor = input('digite um ou mais valores a serem modificados\n')
    valor = int(valor)
    valor2 = input('digite um ou mais valores a serem modificados\n')
    valor2 = int(valor2)
    break
calculadora = True
while calculadora:
    print("digite uma das opções a sequir")
    print("(1) fechar o programa")
    print("(2) soma")
    print("(3) subtração")
    print("(4) divisão")
    print("(5) raiz")
    print("(6) potenciação")
    print('(7) multiplicação')
    opcao = int(input(' '))
    if opcao == 1:
        calculadora = False
    elif opcao == 2:
        print(f'soma entre eles é {(valor + valor2)}')
    elif opcao == 3:
        print(f'a subtração entre eles é {(valor - valor2)}')
    elif opcao == 4:
        print(f'a divisão entre eles é {(valor / valor2)}')
    elif opcao == 5:
        print(f'a raiz de cada um dos valores é de {(math.sqrt(valor), math.sqrt(valor2))}')
    elif opcao == 6:
        print(f'a potenciação dos valores digitados é {(valor ** valor2)}')
    elif opcao == 7:
        print(f'a multiplicação dos items é {(valor * valor2)}')
print('obrigado por tudo.')
