"""Cada degrau de uma escada tem Xcm de
altura. Faça um algoritmo que receba a
altura de cada degrau em cm e a altura que
o usuário deseja alcançar subindo a escada
(em metros). Faça as conversões, calcule e
mostre quantos degraus o usuário deverá
subir para atingir seu objetivo.
Obs: não se preocupe com a altura do
usuário!
"""
# Solicitar ao usuario

altura = float(input("Qual altura, em metros, você quer chegar? "))
tamanho = float(input("Qual a altura, em cm, de cada degrau? "))

# Calcular
total_degrais = altura * (100 / tamanho)

print(f"Você precisa subir {total_degrais} degraus.")