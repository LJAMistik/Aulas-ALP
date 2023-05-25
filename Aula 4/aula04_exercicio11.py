"""Sabe-se que:
1 pé = 12 polegadas
1 jarda = 3 pés
1 milha = 1760 jardas
Faça um algoritmo que receba uma medida
em pés, faça as conversões a seguir e
mostre os resultados:
a) Polegadas
b) Jardas
c) milhas
"""

# Pedir ao usuário:

valor_usuario = float(input("Digite um valor: "))

# converter centimetros em pés
pes_conv = valor_usuario * 30.48
print(f"O Valor digitado em pés é: {pes_conv}")

# converter pes em polegadas
polegas_conv = pes_conv * 12
print(f" O valor digitado em polegadas é {polegas_conv}")

# converter em jardas
jardas_conv = pes_conv * 3
print(f" O valor digitado em jardas é {jardas_conv}")

# convereter em milhas
milhas_conv = jardas_conv * 1760
print(f" O valor digitado em milhas é {milhas_conv}")


