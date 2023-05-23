"""Faça um algoritmo que carregue um vetor de
10 elementos numéricos inteiros.
Após a finalização da entrada, o algoritmo
deve escrever o mesmo vetor, na ordem
inversa de entrada
"""
# Carregar o vetor de entrada
vetor = []
for i in range(10):
    valor = int(input("Digite o valor do vetor: "))
    vetor.append(valor)

# Escrever o vetor na ordem inversa
print("Vetor na ordem inversa:")
for i in range(9, -1, -1):
    print(vetor[i])
