"""Sabe-se que o quilowatt de energia custa
um oitavo do salário mínimo. Faça um
algoritmo que receba o valor do salário
mínimo e a quantidade de quilowatts
consumida por uma residência. Calcule e
mostre:
a) O valor, em reais, de cada quilowatt
b) O valor, em reais, a ser pago por essa
residência
c) O valor, em reais, a ser pago com desconto
de 15%
"""
# Pedir ao usuário:
salario_minimo = float(input("Digite o valor do salário mínimo: "))
quilowatts_consumidos = float(input("Digite a quantidade de quilowatts consumidos: "))

# a) Calcular o valor de cada quilowatt em reais
valor_quilowatt = salario_minimo / 8

# b) Calcular o valor a ser pago pela residência
valor_total = valor_quilowatt * quilowatts_consumidos

# c) Calcular o valor a ser pago com desconto de 15%
valor_desconto = valor_total * 0.15
valor_com_desconto = valor_total - valor_desconto

print(f"O valor de cada quilowatt é R$ {valor_quilowatt:.2f}")
print(f"O valor a ser pago pela residência é R$ {valor_total:.2f}")
print(f"O valor a ser pago com desconto de 15% é R$ {valor_com_desconto:.2f}")
