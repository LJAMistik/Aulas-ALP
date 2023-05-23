"""Uma matriz é uma estrutura de dados bidimensional
 que armazena valores em formato de tabela, com linhas e colunas.
Em Python, podemos representar uma matriz como uma lista de listas,
onde cada lista interna representa uma linha da matriz."""
#Exemplo:
#Criando uma matriz 2x3 com valores iniciais
matriz = [[1, 2, 3], [4, 5, 6]]

"""Você pode acessar elementos específicos de uma matriz usando índices.
Os índices em Python começam em 0. Veja um exemplo:"""
import numpy as np

# Criar uma matriz 2x3 com números inteiros
matriz = np.array([[1, 2, 3], [4, 5, 6]])

# Acessar elementos específicos
print(matriz[0, 0])  # Acessar o elemento na primeira linha e primeira coluna (1)
print(matriz[1, 2])  # Acessar o elemento na segunda linha e terceira coluna (6)

"""Operações com matrizes
Você pode realizar várias operações matemáticas em matrizes usando o NumPy. 
Por exemplo, você pode somar, subtrair, multiplicar e dividir matrizes. 
Veja alguns exemplos:"""

import numpy as np

# Criar duas matrizes 2x3 com números inteiros
matriz1 = np.array([[1, 2, 3], [4, 5, 6]])
matriz2 = np.array([[7, 8, 9], [10, 11, 12]])

# Soma de matrizes
soma = matriz1 + matriz2
print("Soma de matrizes:")
print(soma)

# Subtração de matrizes
subtracao = matriz1 - matriz2
print("Subtração de matrizes:")
print(subtracao)
