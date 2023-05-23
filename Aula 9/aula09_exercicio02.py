"""Faça um algorimto que carregue um vetor de
10 elementos numéricos inteiros.
Após a finalização da entrada, o algoritmo
deve escrever o maior valor e sua posição.
"""
# Declaração do vetor
vetor = []

# Entrada de dados do vetor
for i in range(10):
    valor = int(input("Digite o valor do elemento: "))
    vetor.append(valor)

# Encontra o maior valor e sua posição
maior_valor = vetor[0]
posicao_maior_valor = 0

for i in range(1, 10):
    if vetor[i] > maior_valor:
        maior_valor = vetor[i]
        posicao_maior_valor = i

# Saída de dados do maior valor e sua posição
print("O maior valor é:", maior_valor)
print("Sua posição no vetor é:", posicao_maior_valor)


