"""Faça um algoritmo que receba a data de
nascimento de uma pessoa e a data atual
e mostre sua idade em anos, meses,
semanas e dias
"""
# Ler a data de nascimento
dia_nascimento, mes_nascimento, ano_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ").split('/')

# Ler a data atual
dia_atual, mes_atual, ano_atual = input("Digite a data atual (dd/mm/aaaa): ").split('/')

# Calcular a diferença entre o ano atual e o ano de nascimento
idade_anos = int(ano_atual) - int(ano_nascimento)

# Calcular a diferença de meses
idade_meses = int(mes_atual) - int(mes_nascimento)

# Utilizar aritmética modular para ajustar a idade em anos e meses
idade_anos -= idade_meses // 12
idade_meses = idade_meses % 12

# Calcular a diferença de semanas
dias_totais_nascimento = int(dia_nascimento) + int(mes_nascimento) * 30 + int(ano_nascimento) * 365
dias_totais_atual = int(dia_atual) + int(mes_atual) * 30 + int(ano_atual) * 365
idade_semanas = (dias_totais_atual - dias_totais_nascimento) // 7

# Calcular a diferença de dias
idade_dias = (dias_totais_atual - dias_totais_nascimento) % 7

# Exibir a idade em anos, meses, semanas e dias
print("Idade:")
print("Anos:", idade_anos)
print("Meses:", idade_meses)
print("Semanas:", idade_semanas)
print("Dias:", idade_dias)
