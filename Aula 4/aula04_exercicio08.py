"""Faça um algoritmo que calcule e mostre a
área de um triângulo. Sabe-se que Área =
(base * altura)/2
"""

# Pedir ao usuário os valores de base e altura do triangulo:
altura = float(input("Digite o valor de altura deste triângulo: "))
base = float(input("Digite o valor da base deste triângulo: "))

# Calcular:
area_triangulo = base * altura // 2

# Mostrar o resultado do calculo:

print("O resultado é: ", area_triangulo)
