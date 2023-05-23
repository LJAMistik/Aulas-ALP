"""Faça um algoritmo que armazenará os 10
primeiros números primos acima de 100. Ao
final, o algoritmo deve mostrar os valores
desse vetor."""

# Inicio do vetor e variavel

numeros_primos = []
numero = 101 # Primeiro número a ser verificado

# Buscar os números primos acima de 100

while len(numeros_primos) < 10: # Enquanto não tivermos 10 números primos
    # Verificar se o número atual é primo
    is_primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            is_primo = False
            break

    if is_primo:
        numeros_primos.append(numero)  # Adicionar o número primo ao vetor

    numero += 1  # Incrementar o número para a próxima verificação

# Mostrar no prompt
print("Os 10 primeiros números primos acima de 100 são:")
for numero_primo in numeros_primos:
    print(numero_primo)
