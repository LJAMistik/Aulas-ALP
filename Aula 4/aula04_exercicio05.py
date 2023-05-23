"""Faça um algoritmo que receba o salário de
um funcionário, calcule e mostre o novo 
salário, sabendo-se que este sofreu um 
aumento de 25%."""

# Pedir o valor do salário:
salario = float(input("Digite o valor do seu salário em R$: "))

# Fazer o calculo:
reajuste = salario * 0.25 # Não existe porcentagem em python, precisa converter.

# Juntar numa varíavel pra poder mostrar:
total_salario = reajuste + salario
print(f"Seu salário foi reajustado para: R$ {total_salario:.2f}")# o uso de :.2f serve para mostrar duas casas decimais.
