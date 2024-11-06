alunos = ["Simone","Vanessa","Fernando","Ricardo"] #lista
# indices:    0         1          2         3
#O [] (lista) é ordenado.
turma = {"Simone","Vanessa","Fernando","Ricardo"} #set
# o {} (set) é desordenado, sem elemento repetido.
#print(alunos)
#print(turma)
print(alunos[1])
print(alunos)
alunos[1] = "Vanessa Azevedo"
#Acima é uma tribuição de um novo comando 
print(alunos)

#Adicionar valor em lista
alunos.extend(["Gustavo"])
print(alunos)
#adicionar um registro em lista
alunos.append("Aurélio")
print(alunos)
#Com o insert também é possivél inserir e especificar a posição que se quer na lista.
alunos.insert(0,"Maria Eduarda")
print(alunos)
#Para remover com remove, não usar colchete.Com ele da para especificar quem/o quê se quer eliminar. 
alunos.remove("Simone")
print(alunos)
#O pop remove do final para o início.
alunos.pop()
print(alunos)
#Apgar conteúdo de uma lista
#alunos.clear()
#print(alunos)
#Ordenar lista é com o sort:
alunos.sort()
print(alunos)
