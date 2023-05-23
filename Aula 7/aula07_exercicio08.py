"""Faça um programa que receba um número inteiro maior 
que 1. Ele deve verificar se o número fornecido é primo 
ou não, e mostrar a mensagem correspondente.
Lembre-se: um número primo só é divisível por 1 ou por 
ele mesmo"""

def verificar_primo(numero):
    if numero < 2:
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True

numero = int(input("Digite um número inteiro maior que 1: "))

if verificar_primo(numero):
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")
