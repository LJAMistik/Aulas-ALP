"""Faça uma função que retorne o valor lógico V 
(verdadeiro) se o número inteiro passado por 
parâmetro for primo, e F (falso) se não.
Implemente sua função em um programa 
completo.
"""

def verificar_primo(numero):
    if numero < 2: #numeros menores que 2 não são primos
        return False

    for i in range(2, int(numero ** 0.5) + 1): # O loop for itera de 2 até a raiz quadrada do número + 1 para verificar se o número é divisível por algum valor nesse intervalo, retornando False se for encontrado um divisor.
        if numero % i == 0:
            return False

    return True

# Exemplo de uso da função:
numero = int(input("Digite um número inteiro: "))
resultado = verificar_primo(numero)

if resultado:
    print("O número é primo.")
else:
    print("O número não é primo.")


""" Encontrar os 50 primeiros números primos """
numeros_primos = [] # lista vazia
numero = 2
while len(numeros_primos) < 50:
    if verificar_primo(numero):
        numeros_primos.append(numero) #append permite adicionar o elemento no final da lista, para ser mostrado no final.
    numero += 1 #incrementar 1 numero ao valor anterior para avançar no loop

# Imprimir os 50 primeiros números primos
print("Os 50 primeiros números primos:")
for numero_primo in numeros_primos:
    print(numero_primo)
