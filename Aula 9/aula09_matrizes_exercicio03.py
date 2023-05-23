"""Faça um algoritmo que leia os dados de uma
matriz de 4 linhas e 4 colunas, composta de
elementos reais, e calcule a soma dos
elementos da diagonal principal da matriz."""

# Lê os elementos da matriz 4x4
matriz = []
for i in range(4):
    linha = []
    for j in range(4):
        elemento = float(input(f"Digite o elemento [{i+1},{j+1}]: "))
        linha.append(elemento)
    matriz.append(linha)

# Calcula a soma dos elementos da diagonal principal
soma_diagonal = 0
for i in range(4):
    soma_diagonal += matriz[i][i]

# Mostra a soma dos elementos da diagonal principal
print(f"Soma dos elementos da diagonal principal: {soma_diagonal}")
