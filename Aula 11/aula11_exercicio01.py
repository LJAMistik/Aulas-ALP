"""Faça um algoritmo que carregue uma tupla 
de 10 elementos numéricos inteiros.
Após a finalização da entrada, o algoritmo 
deve escrever a mesma tupla, na ordem 
inversa de entrada.
"""

# Carregar a tupla de entrada
tupla_entrada = []
for i in range(10):
    elemento = int(input("Digite um elemento inteiro: "))
    tupla_entrada.append(elemento)

# Obter a tupla inversa
tupla_inversa = tuple(reversed(tupla_entrada))

# Mostrar no prompt a tupla inversa
print("Tupla na ordem inversa:")
for elemento in tupla_inversa:
    print(elemento)
