"""Elabore um algoritmo para ler/receber, 
separadamente, o primeiro nome, o nome do 
meio e o sobrenome de uma pessoa, e mostre 
o nome completo, correspondente"""

# Leitura dos nomes separadamente
primeiro_nome = input("Digite o primeiro nome: ")
nome_meio = input("Digite o nome do meio: ")
sobrenome = input("Digite o sobrenome: ")

# Construção do nome completo (concatenação + e espaço)
nome_completo = primeiro_nome + " " + nome_meio + " " + sobrenome

# Exibição do nome completo
print("Nome completo: " + nome_completo)
