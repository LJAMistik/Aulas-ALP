"""Faça um algoritmo que leia uma matriz 2x2,
calcule e mostre uma matriz resultante que
será a matriz digitada, multiplicada pelo
maior elemento da matriz"""

# Lê os elementos da matriz 2x2
matriz = []
for i in range(2):
    linha = []
    for j in range(2):
        elemento = int(input(f"Digite o elemento [{i+1},{j+1}]: "))
        linha.append(elemento)
    matriz.append(linha)

# Encontra o maior elemento da matriz
maior_elemento = matriz[0][0]
for linha in matriz:
    for elemento in linha:
        if elemento > maior_elemento:
            maior_elemento = elemento

# Calcula a matriz resultante e multiplica pelo maior elemento
matriz_resultante = []
for linha in matriz:
    linha_resultante = []
    for elemento in linha:
        elemento_resultante = elemento * maior_elemento
        linha_resultante.append(elemento_resultante)
    matriz_resultante.append(linha_resultante)

# Mostrar no prompt a matriz resultante

print("Matriz digitada: ")
for linha in matriz:
    print(linha)

print("Matriz resultante: ")
for linha in matriz_resultante:
    print(linha)
