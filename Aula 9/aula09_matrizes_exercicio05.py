"""Faça um algoritmo que receba uma matriz 10x10
de elementos inteiros e localize a posição (linha
e coluna) do maior elemento da matriz"""

# Cria a matriz 10x10 com elementos inteiros
matriz = []
for i in range(10):
    linha = []
    for j in range(10):
        elemento = int(input(f"Digite o elemento da matriz [{i+1},{j+1}]: "))
        linha.append(elemento)
    matriz.append(linha)

# Encontra o maior elemento e sua posição
maior_elemento = matriz[0][0]
linha_maior = 0
coluna_maior = 0

for i in range(10):
    for j in range(10):
        if matriz[i][j] > maior_elemento:
            maior_elemento = matriz[i][j]
            linha_maior = i
            coluna_maior = j

# Mostra a posição do maior elemento
print(f"O maior elemento da matriz é: {maior_elemento}")
print(f"Sua posição (linha, coluna) é: ({linha_maior + 1}, {coluna_maior + 1})")
