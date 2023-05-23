"""Faça um algoritmo que leia um valor N inteiro 
e positivo, calcule e mostre o valor E, 
conforme a fórmula a seguir.
E = (2 ** 1) + (2 ** 2) + (2 ** 3) + ... + (2 ** N)
"""

N = int(input("Digite um valor inteiro e positivo: "))

# Inicializar o valor de E
E = 0

# Calcular o valor de E usando a fórmula
for i in range(1, N + 1):
    E += 2 ** i

print("Esse valor 'E' será calculado da seguinte forma: E = 2^1 + 2^2 + 2^3 + ... + 2^N, onde N é o valor que você escolheu")

# Mostrar o valor de E
print("Então o valor de E é:", E)
