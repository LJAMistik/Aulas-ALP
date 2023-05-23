"""Faça um algorimto que carregue um 
dicionário de 10 elementos onde a chave é o 
sobrenome da pessoa e o valor a sua idade.
Após a finalização da entrada, o algoritmo 
deve escrever o sobrenome da pessoa com 
maior idade.
"""

# Carregar o dicionário de entrada
dicionario = {}
for i in range(10):
    sobrenome = input("Digite o sobrenome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    dicionario[sobrenome] = idade

# Encontrar o sobrenome da pessoa com maior idade
maior_idade = max(dicionario.values())
sobrenome_maior_idade = [key for key, value in dicionario.items() if value == maior_idade][0]

# Imprimir o sobrenome da pessoa com maior idade
print("Sobrenome da pessoa com maior idade:", sobrenome_maior_idade)
