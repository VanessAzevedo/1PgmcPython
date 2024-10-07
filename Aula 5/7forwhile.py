lista = []

while True:
    numero = int(input("Digite um número (0 - sai: "))
    if numero == 0:
        break #ele sai da estrutura, sai do while

    lista.append(numero)
print(lista)

#O WHILE não pode sere convertido em FOR porque
#o número de repetições é desconhecido no início
for i in lista:
    print(i)
    