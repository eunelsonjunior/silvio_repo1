# 7. LISTAS DENTRO DE LISTAS
#   Faça um programa que crie uma matriz 3x3 (3 linhas e 3 colunas) preenchida com números 
#   fornecidos pelo usuário. No final, exiba a matriz na tela e mostre:
#   - A soma de todos os elementos
#   - A soma da primeira linha
#   - A soma da diagonal principal

n = 3
matriz = []
for i in range(n):
    matriz.append([])
    for j in range(n):
        matriz[i].append(int(input(f"Digite um nũmero para a posição ({i}, {j}): ")))

soma_todos = sum([matriz[i][j] for i in range(n) for j in range(n)])
soma_prim_linha = sum(matriz[0])
soma_diag_prin = sum([matriz[k][k] for k in range(n)])

print(f"Soma de todos os elementos: {soma_todos}")
print(f"Soma da primeira linha: {soma_prim_linha}")
print(f"Soma da diagonal principal: {soma_diag_prin}")