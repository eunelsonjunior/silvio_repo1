# 5. MÉDIA E ACIMA
#   Crie um programa que leia as notas de uma turma (quantidade indefinida). 
#   O programa deve parar quando o usuário digitar -1. 
#   Calcule a média da turma e mostre quantos alunos obtiveram nota acima dessa média.

notas = []
while(True):
    nota = float(input("Digite uma nota ou -1 para encerrar: "))
    if (nota == -1.0):
        break
    notas.append(nota)
media = sum(notas)/len(notas)
acima_media = sum([1 if n > media else 0 for n in notas])
print(f"Média: {media:.1f}")
print(f"Alunos acima da média: {acima_media}")