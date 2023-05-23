"""Faça um programa que calcule os 10 primeiros números 
da sequencia de Fibonacci
"""

def calcular_fibonacci(n):
    fibonacci = [0, 1]  # Inicializamos com os dois primeiros números da sequência

    for i in range(2, n):
        # Calculamos o próximo número da sequência somando os dois anteriores
        proximo = fibonacci[i - 1] + fibonacci[i - 2]
        fibonacci.append(proximo)

    return fibonacci

n = 10  # Número de elementos da sequência que desejamos calcular
resultado = calcular_fibonacci(n)
print(resultado)
