"""Faça algoritmo que carregue dois vetores de
dez elementos numéricos cada um e mostre
um vetor resultante na intercalação desses
dois vetores"""

# Declaração dos vetores
vetor1 = []
vetor2 = []
vetorResultado = []

# Entrada de dados do vetor1
for i in range(10):
    valor = int(input("Digite o valor do elemento do vetor1: "))
    vetor1.append(valor)

# Entrada de dados do vetor2
for i in range(10):
    valor = int(input("Digite o valor do elemento do vetor2: "))
    vetor2.append(valor)

# Intercalação dos vetores
indice1 = 0
indice2 = 0
while indice1 < 10 and indice2 < 10:
    if vetor1[indice1] < vetor2[indice2]:
        vetorResultado.append(vetor1[indice1])
        indice1 += 1
    else:
        vetorResultado.append(vetor2[indice2])
        indice2 += 1

# Copia os elementos restantes do vetor1, se houver
while indice1 < 10:
    vetorResultado.append(vetor1[indice1])
    indice1 += 1

# Copia os elementos restantes do vetor2, se houver
while indice2 < 10:
    vetorResultado.append(vetor2[indice2])
    indice2 += 1

# Saída de dados do vetor resultante
print("O vetor resultante da intercalação dos vetores é:", vetorResultado)
