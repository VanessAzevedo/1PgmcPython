'''Elabore um fluxograma que calcule quantas notas de 50, 10 e 1
são necessárias para se pagar uma conta cujo valor é fornecido.'''
#Configurando o programa para saber se o usuário deseja efetuar outro saque:

while True:
    valor = int(input("Digite o valor da conta: "))

    n50 = valor//50
    r50 = valor % 50
    n10 = r50//10
    n1 = r50 % 10

    print('Notas de 50 é',n50)
    print('Notas de 10 é',n10)
    print('Moedas de 1 é',n1)

    resposta = input('Deseja fazer outro saque (Sim/Não)? ')
    if resposta == 'não':
        break