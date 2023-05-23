"""Faça um algoritmo que simule a jogada de dois
dados de 6 faces. O programa deve usar randint
para rolar o primeiro dado e deve usar randint
novamente para rolar o segundo dado. A soma
das duas faces deve ser calculada. Assim: a
soma variará de 2 a 12
O programa deve rolar 30.000 vezes e mostrar
a frequência com que a soma (de 2 a 12)
aparecem. Verifique se o valor 7 corresponde a
1/6 das jogadas!
"""
import random

# Inicializa o contador de frequência para cada soma possível
frequencia = [0] * 11

# Simula 30.000 jogadas de dois dados de 6 faces
for i in range(30000):
    dado1 = random.randint(1, 6)  # Rola o primeiro dado
    dado2 = random.randint(1, 6)  # Rola o segundo dado
    soma = dado1 + dado2  # Calcula a soma das faces dos dois dados
    frequencia[soma-2] += 1  # Incrementa a frequência da soma na posição correspondente do contador

# Mostra no prompt
print("Frequência das somas (de 2 a 12):")
for soma, valor in enumerate(frequencia, start=2):
    print("Soma", soma, ":", valor)

# Verifica se o valor 7 corresponde a 1/6 das jogadas
frequencia_7 = frequencia[5]  # Frequência da soma 7 (posição 5 no contador)
percentual_7 = (frequencia_7 / 30000) * 100  # Frequência percentual da soma 7
print("Frequência do valor 7:", frequencia_7)
print("Percentual do valor 7:", percentual_7)

if abs(percentual_7 - (1 / 6 * 100)) < 1:
    print("O valor 7 corresponde a aproximadamente 1/6 das jogadas.")
else:
    print("O valor 7 não corresponde a aproximadamente 1/6 das jogadas.")