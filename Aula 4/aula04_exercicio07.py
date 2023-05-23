"""Faça um algoritmo que receba o valor de
um depósito e o valor da taxa de juros,
calcule e mostre o valor do rendimento e
o valor total depois do rendimento.
"""
# Pedir ao usuário:
deposito = float(input("Digite o valor que deseja depositar em R$: "))
juros = float(input("Digite o valor percentual da taxa de juros: "))

# Calcular
juros_conv = deposito * juros // 100
rendimento = juros_conv
total_rendimentos = deposito + juros_conv

#Mostrar os valores:
print(f"O valor do rendimento dos juros é de R$ {rendimento:.2f}")
print(f"O valor total do seu rendimento é de R$ {total_rendimentos:.2f}")