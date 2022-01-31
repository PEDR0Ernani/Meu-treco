import math
quant = opcao = 0
valores = [0]

while True:
    valor = input('digite um ou mais valores a serem modificados\n')
    quali = valor.isnumeric()
    if not quali:
        print('erro, seu valor precisa ser númerico')
    valores.append(valor)
    quant += 1
    if quant >= 2:
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
    opcao = int(input(' '))
    if opcao == 1:
        calculadora = False
    elif opcao == 2:
        print(f'soma entre eles é {(valores[0] * valores[1])}')
    elif opcao == 3:
        print(f'a subtração entre eles é {(valores[0] - valores[1])}')
    elif opcao == 4:
        print(f'a divisão entre eles é {(valores[0] / valores[1])}')
    elif opcao == 5:
        print(f'a raiz de cada um dos valores é de {(math.sqrt(valores[0]), math.sqrt(valores[1]))}')
    elif opcao == 6:
        print(f'a potenciação dos valores digitados é {(valores[0] ** valores[1])}')
print('obrigado por tudo.')
