"""Faça um algoritmo para determinar quantas 
palavras existem em uma determinada frase 
Obs: tanto a palavra, quanto a frase, devem 
ser informadas pelo usuário.
"""

frase = input("Digite uma frase: ")

# Quebrar a frase em palavras
palavras = frase.split()

# Obter o número de palavras
numero_palavras = len(palavras)

print("Número de palavras na frase:", numero_palavras)
