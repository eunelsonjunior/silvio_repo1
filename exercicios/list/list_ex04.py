# 4. INVERTENDO A LISTA
#   Escreva um programa que leia 6 palavras e as armazene em uma lista. 
#   Em seguida, exiba a lista na ordem inversa sem usar o método reverse() ou fatiamento [::-1].

n = 6
lista = []
for i in range(n):
    lista.append(input(f"Digite a {i+1}ª palavra: "))
for i in range(n):
    print(lista[n-i-1], end=" ")