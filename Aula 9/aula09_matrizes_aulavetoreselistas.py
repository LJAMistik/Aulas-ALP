"""Vetores e Listas

São Estruturas de Dados

Vetores: Sequencia de valores de mesmo tipo de dados, guardados em uma mesma varíavel.
É necessário utilizar a biblioteca numpy:"""

import numpy as np

# Criando um vetor
vetor = np.array([1, 2, 3, 4, 5])

#Nesse exemplo foi definido o vetor com esses valores, pode ser acessado usando o indice:

# Acessando elementos do vetor
print(vetor[0]) # Saída: 1
print(vetor[3]) # Saída: 4

"""
Listas: Armazenam uma coleção de elementos de diferentes tipos de dados, é mutável, ao contrário da string."""
# Criando uma lista
lista = [1, 2, 3, 4, 5]

# Acessando elementos da lista, usando o indice:
print(lista[0]) # Saída: 1
print(lista[3]) # Saída: 4

""" suportam várias operações de manipulação, por exemplo:"""

# Adicionando um elemento à lista
lista.append(6)

# Removendo um elemento da lista
lista.remove(3)

# Modificando um elemento da lista
lista[0] = 0

# Obtendo o tamanho da lista
tamanho = len(lista)

# Verificando se um elemento está na lista
if 4 in lista:
    print("4 está na lista!")

