"""Faça um algoritmo para ler nove caracteres 
numéricos em uma string. Mostre o conteúdo 
dessa string colando pontos e virgula, 
respectivamente nas posições inteiras e 
decimais. 
Exemplo: 
Digitado> 987654321
Mostrado> 9.876.543,21
"""

numeros = input("Digite nove caracteres numéricos: ")

# Verificar se a string possui nove caracteres
if len(numeros) != 9:
    print("A string deve conter exatamente nove caracteres.")
else:
    # Separar parte inteira e parte decimal
    parte_inteira = numeros[:6]
    parte_decimal = numeros[6:]

    # Adicionar pontos e vírgula
    nova_string = parte_inteira[:3] + '.' + parte_inteira[3:] + ',' + parte_decimal

    print("Mostrado:", nova_string)
