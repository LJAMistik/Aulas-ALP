"""Faça um programa que receba um número inteiro x. 
Calcule e mostre o fatorial desse número (x!)"""

def calcular_fatorial(numero):
    fatorial = 1

    if numero < 0:
        return "Erro: Não é possível calcular o fatorial de um número negativo."
    elif numero == 0:
        return 1
    else:
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial

numero = int(input("Digite um número inteiro: "))
resultado = calcular_fatorial(numero)
print(f"O fatorial de {numero} é {resultado}.")
