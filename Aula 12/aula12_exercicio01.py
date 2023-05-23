'''Faça uma função que retorne o valor lógico V 
(verdadeiro) se o número inteiro passado por 
parâmetro for par, e F (falso) se não.
Implemente sua função em um programa 
completo.
'''

def verificar_par(numero):
    if numero % 2 == 0:
        return "Verdadeiro"  # número é par
    else:
        return "Falso"  # número é ímpar

# Exemplo de uso da função:
numero = int(input("Digite um número inteiro: "))
resultado = verificar_par(numero)
print("O número é par? Resposta:", resultado)
