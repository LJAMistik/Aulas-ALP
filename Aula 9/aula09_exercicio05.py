"""Faça um Algoritmo que simule 6000 jogadas
de um dado de 6 faces. Para simular o
resultado utilize a função randint
Ao final, mostre a frequência de sorteio de
cada uma das faces"""
import random # biblioteca que gera os números aleatórios

# Inicializa o contador de frequência para cada face
frequencia = [0, 0, 0, 0, 0, 0]

# Simula 6000 jogadas de um dado de 6 faces
for i in range(6000):
    resultado = random.randint(1, 6)  # Gera um número aleatório entre 1 e 6 (inclusive)
    frequencia[resultado-1] += 1  # Incrementa a frequência do resultado na posição correspondente do contador

# Mostra a frequência de sorteio de cada face
for i in range(6):
    print("Frequência de sorteio de cada face:")
    for face, valor in enumerate(frequencia):
        print("Face", face + 1, ":", valor)
