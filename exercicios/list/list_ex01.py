# 1. SOMA DOS ELEMENTOS
#   Escreva um programa que crie uma lista com 5 números inteiros fornecidos pelo usuário 
#   e exiba a soma de todos os elementos.

n = 5
lista = []
for i in range(n):
    lista.append(int(input(f"Digite o {i+1}º número: ")))
print(sum(lista))