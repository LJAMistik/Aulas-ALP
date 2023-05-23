"""Faça um algoritmo para determinar se um 
determinado vetor, digitado pelo usuário, é 
um palíndromo.
Palíndromo: lido da direita para a esquerda, 
ou vice versa, representam a mesma coisa.
Ex: AMA"""

vetor = input("Digite um vetor: ")

# Verificar se o vetor é um palíndromo
if vetor == vetor[::-1]:
    print("O vetor é um palíndromo.")
else:
    print("O vetor não é um palíndromo.")
