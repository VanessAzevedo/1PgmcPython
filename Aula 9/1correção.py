resposta = int(input("Quantos alunos para calcular? "))

i = 0
alunos = []

while i < resposta:
    nomeAluno = input('Digite o nome do aluno: ')
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2)

    resultado = "Aprovado" if media >= 6.5 else "Reprovado"

    alunos.append(
        {
        'nome': nomeAluno,
        'nota1': nota1,
        'nota2': nota2,
        'media': media,
        'resultado': resultado
    }
    )
    i = i + 1

for aluno in alunos:
    print(aluno['nome'],'(Média:',aluno['media'],' - ',aluno['resultado'],')')

