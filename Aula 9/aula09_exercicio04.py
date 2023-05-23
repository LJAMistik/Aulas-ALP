"""Faça um algoritmo que leia 20 palavras de no
máximo 10 caracteres, e após a leitura, realize
um processo qualquer que inverta os
caracteres de cada uma das palavras.
"""
# Ler as 20 palavras
palavras = []
for i in range(20):
    palavra = input("Digite a palavra {}: ".format(i+1))
    palavras.append(palavra)

# Inverter os caracteres de cada palavra
palavras_invertidas = []
for palavra in palavras:
    palavra_invertida = palavra[::-1]
    palavras_invertidas.append(palavra_invertida)

# Mostrar as palavras invertidas
print("Palavras invertidas:")
for palavra_invertida in palavras_invertidas:
    print(palavra_invertida)
