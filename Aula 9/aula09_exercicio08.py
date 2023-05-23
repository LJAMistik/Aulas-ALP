"""Faça um algoritmo que lê 10 números inteiros e
os armazena em um vetor A.
Depois de armazenado, o algoritmo fará a
ordenação desses números (em ordem
crescente de valores) e os colocará no vetor B
Ao final o algoritmo deve mostrar os dois
vetores: A e B.
"""
# Lê 10 números inteiros e armazena no vetor A
vetor_A = []
for i in range(10):
    numero = int(input("Digite o número {}: ".format(i + 1)))
    vetor_A.append(numero)

# Ordena os números no vetor A em ordem crescente
vetor_B = sorted(vetor_A)

# Mostra os vetores A e B
print("Vetor A: ", vetor_A)
print("Vetor B: ", vetor_B)
