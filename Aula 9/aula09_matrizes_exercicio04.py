"""Faça um algoritmo que leia os valores de uma
matriz 3x3 de elementos reais e crie a matriz
transposta da matriz fornecida.
Matriz transposta: Igual a simétrica. Em
matemática, é o resultado da troca de linhas por
colunas em uma determinada matriz.
A[i,j] = A[j,i"""

# Lê os elementos da matriz 3x3
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        elemento = float(input(f"Digite o elemento [{i+1},{j+1}]: "))
        linha.append(elemento)
    matriz.append(linha)

# Cria a matriz transposta
matriz_transposta = []
for i in range(3):
    linha_transposta = []
    for j in range(3):
        linha_transposta.append(matriz[j][i])
    matriz_transposta.append(linha_transposta)

# Mostra a matriz transposta
print("Matriz Transposta:")
for linha in matriz_transposta:
    print(linha)
