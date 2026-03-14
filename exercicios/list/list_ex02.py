# 2. MAIOR E MENOR VALOR
#   Crie um programa que leia 7 números inteiros, armazene-os em uma lista e mostre 
#   o maior e o menor valor digitados, juntamente com suas respectivas posições.

n = 7
lista = []
for i in range(n):
    lista.append(int(input(f"Digite o {i+1}º número: ")))
maior = max(lista)
menor = min(lista)
print(f"Maior: {maior} ({lista.index(maior) + 1}º número)")
print(f"Menor: {menor} ({lista.index(menor) + 1}º número)")