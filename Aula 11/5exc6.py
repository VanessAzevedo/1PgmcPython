'''Tendo como dados de entrada a alura e o sexo de uma pessoa
('M' masculino e 'f' feminino), construa um algoritmo que calcule seu peso ideal, utilizndo as seguintes fórmulas:
para homens: (72.7 * altura) - 58 e para mulheres: (62.1 * altura) - 44.7'''


h = float(input('Digite sua altura: '))
sexo = input('Informe o sexo (feminino/maculino:) ')

if (sexo == 'masculino'):
    peso = (72.7 * h) - 58
else:
    peso = (62.1 * h) - 44.7

print('O seu peso ideal é',peso)




