# solicito o usuário para digitar um número
numero = int(input("Digite um número para tabuada de 10"))
#inicializo o número
i = 1
# estrutura de repetição 
while i <= 10:
    aux = i * numero
    print(i, "x", numero , "=", aux)
    i = i + 1
