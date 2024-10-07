"""escreva um programa que leia dois números
e que pergunte qual operação voce deseja realizar.
voce deve poder calcular
soma(+), subtração(-), multiplicação(*)  e divisão(/).
Exiba o resultado da operação solicitada."""

#Entrada
num1 = int(input("Digite o primeiro número para calculo: "))
num2 = int(input("Digite o segundo número: "))
operacao = input("Deseja realizar soma (+), subtração (-), multiplicação (*) e divisão (/)")
#Processamento
if operacao == "+":
   resultado = num1 + num2
elif operacao == "-":
   resultado = num1 - num2
elif operacao == "*":
   resultado = num1 * num2
elif operacao == "/":
   resultado = num1 / num2
else:
   print("Operação inválida.")
   resultado = 0 
print("Resultado: ",resultado)
