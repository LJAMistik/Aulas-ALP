"""Faça um algoritmo que receba o salário de
um funcionário e o percentual de aumento,
calcule e mostre o valor do aumento e o
novo salário."""

# Pedir o valor do salário:
salario_inicial = float(input("Digite o valor do seu salário em R$: "))

# Pedir o percentual de aumento do salário:
percentual_aumento = float(input("Digite o valor do percentual do aumento de seu salário: "))

# Calcular:
percentual_aumento_conv = percentual_aumento / 100
aumento = salario_inicial * percentual_aumento_conv
salario_novo = salario_inicial + aumento
print(f"O valor do aumento é de R$ {aumento}")
print(f"O valor atualizado do seu salário é de R$ {salario_novo:.2f}")