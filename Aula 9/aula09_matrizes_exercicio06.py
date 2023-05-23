"""Faça um algoritmo que leia uma matriz 10x20
com números inteiros e some cada uma das
linhas, armazenando o resultado das somas em
um vetor. A seguir, multiplique cada elemento
da matriz pela soma da linha e mostre a matriz
resultante.
"""

# Importa a biblioteca NumPy para trabalhar com matrizes
import numpy as np

# Cria a matriz 10x20 com números inteiros
matriz = np.zeros((10, 20), dtype=int)
for i in range(10):
    for j in range(20):
        matriz[i][j] = int(input(f"Digite o elemento da matriz [{i+1},{j+1}]: "))

# Calcula a soma de cada linha e armazena em um vetor
soma_linhas = []
for i in range(10):
    soma = np.sum(matriz[i])
    soma_linhas.append(soma)

# Multiplica cada elemento da matriz pela soma da linha correspondente
matriz_resultante = np.zeros((10, 20), dtype=int)
for i in range(10):
    for j in range(20):
        matriz_resultante[i][j] = matriz[i][j] * soma_linhas[i]

# Mostra a matriz resultante
print("Matriz resultante:")
print(matriz_resultante)
