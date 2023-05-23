"""Faça algoritmo que carregue duas listas de dez 
elementos numéricos inteiros cada um. A 
partir dessas duas listas, crie um conjunto da 
união entre essas duas listas"""

# Carregar as duas listas de entrada
lista1 = []
lista2 = []

print("Carregando a primeira lista:")
for i in range(10):
    elemento = int(input("Digite um elemento inteiro: "))
    lista1.append(elemento)

print("\nCarregando a segunda lista:")
for i in range(10):
    elemento = int(input("Digite um elemento inteiro: "))
    lista2.append(elemento)

# Criar o conjunto da união entre as duas listas
conjunto_uniao = set(lista1).union(lista2)

# Imprimir o conjunto da união
print("\nConjunto da união:")
for elemento in conjunto_uniao:
    print(elemento)
