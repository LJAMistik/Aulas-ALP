"""Construa um algoritmo que calcule a média
aritmética de um conjunto de números pares que
forem fornecidos pelo usuário. O valor de
finalização será a entrada do número 0. Observe
que nada impede que o usuário forneça quantos
números ímpares quiser, com a ressalva de que
eles não poderão ser acumulados"""

numeros_pares = []
numero = int(input("Digite um número par (ou 0 para encerrar): "))

while numero != 0:
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        print("Número ímpar fornecido. Apenas números pares são aceitos.")

    numero = int(input("Digite um número par (ou 0 para encerrar): "))

if len(numeros_pares) > 0:
    media = sum(numeros_pares) / len(numeros_pares)
    print("A média dos números pares é:", media)
else:
    print("Nenhum número par foi fornecido.")
