# 8. INTERCALANDO LISTAS
#   Escreva um programa que leia duas listas de 5 elementos cada e gere uma terceira lista 
#   com os elementos intercalados (primeiro da lista A, primeiro da lista B, segundo da lista A, etc.)

n = 5
lista_a = []
lista_b = []
lista_c = []
for i in range(n):
    lista_a.append(input(f"Digite o {i+1}º elemento da Lista A: "))
for i in range(n):
    lista_b.append(input(f"Digite o {i+1}º elemento da Lista B: "))
for i in range(n):
    lista_c.append(lista_a[i])
    lista_c.append(lista_b[i])
print(lista_c)