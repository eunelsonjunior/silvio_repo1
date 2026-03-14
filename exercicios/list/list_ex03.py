# 3. CONTAGEM DE PARES
#   Faça um programa que gere uma lista com 10 números aleatórios entre 1 e 100 
#   e mostre quantos deles são pares.

from random import random

n = 10
numeros = [int(random()*100)+1 for i in range(10)]
pares = [1 if num % 2 == 0 else 0 for num in numeros]
print(numeros)
print(f"Há {sum(pares)} números pares.")