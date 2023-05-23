"""Faça um algoritmo que solicite uma data no 
formato de uma string – dd/mm/aaaa. Mostre 
essa data no formato AAAAMMDD
"""

data = input("Digite uma data (dd/mm/aaaa): ")

# Separar dia, mês e ano
dia, mes, ano = data.split('/')

# Construir a nova data no formato AAAAMMDD
nova_data = ano + mes + dia

print("Data no formato AAAAMMDD:", nova_data)
