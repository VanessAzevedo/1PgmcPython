resposta = int(input('Quantos alunos para calcular? '))

for i in range(resposta):
    nomeAluno = input("Digite o seu nome: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = (nota1 + nota2)/2

    if media >= 6.5:
        print(f"{media} - Aprovado")
    else:
        print(f"{media} - Reprovado")

#Essa é uma estrutura de repetção limitada.