alunos = []
usuario = int(input("Quantos alunos deseja calcular a media: "))
for i in range(usuario):
    nome = input("Nome do aluno: ")
    nota1 = float(input("Primeira nota tirada: "))
    nota2 = float(input("Segunda nota tirada: "))
    media = (nota1 + nota2)/2
    resultado = "Aprovado" if media >= 6.5 else "reprovado"
    alunos.append({
         'nome': nome,
         'nota1': nota1,
         'nota2': nota2,
         'media': media,
         'resultado': resultado
    }
    )
for aluno in alunos:
    print(aluno['nome'],'(Média: ',aluno['media'],' - ',aluno['resultado'],')')
    

