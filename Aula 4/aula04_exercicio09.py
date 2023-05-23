"""Faça um algoritmo que calcule e mostre a
área de um círculo. Sabe-se que
Area= π * R2
π = 3,1415
"""

# Pedir ao usuario o valor do raio
raio_circulo = float(input("Digite o raio do círculo: "))

# Calcular a formula:
Area = 3.1415 * (raio_circulo**2)

# Mostrar o resultado:
print(f"A Area do circulo é: {Area:.2f}")

