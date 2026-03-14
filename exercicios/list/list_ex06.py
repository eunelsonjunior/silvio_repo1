# 6. REMOVENDO DUPLICATAS
#   Desenvolva um programa que receba uma lista de números inteiros (pode ter valores repetidos) 
#   e crie uma nova lista apenas com os valores únicos, mantendo a ordem de primeira aparição.

numeros = []
while(True):
    num = int(input("Digite um número inteiro ou -1 para encerrar: "))
    if (num == -1):
        break
    numeros.append(num)
numeros_unicos = []
for num in numeros:
    if num not in numeros_unicos:
        numeros_unicos.append(num)
for num in numeros_unicos:
    print(num, end=" ")