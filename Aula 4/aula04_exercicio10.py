"""Faça um algoritmo que receba um número
positivo e maior que zero, calcule e mostre:
a) O número digitado ao quadrado
b) O número digitado ao cubo
c) A raiz quadrada do número digitado
Observação:
Exp(x,y) – Calcula a potência de x elevado a y
Raizq(x) – Calcula a raiz quadrada de x"""

numero_digitado = None

while numero_digitado is None:
    entrada = input("Digite um número positivo e maior que zero: ")
    numero_digitado = float(entrada) if entrada.replace('.', '', 1).isdigit() else None

    if numero_digitado is None or numero_digitado <= 0:
        print("Por favor, digite um número positivo e maior que zero.")

print("O número digitado foi:", numero_digitado)

# a)
valor_quadrado = (numero_digitado) ** 2
print(f"O valor ao quadrado é {valor_quadrado}")

# b)
valor_aocubo = (numero_digitado) ** 3
print(f"O valor ao cubo é {valor_aocubo}")

# c)
valor_raizq = (numero_digitado) ** 0.5
print(f"O valor da raiz quadrada é {valor_raizq}")
