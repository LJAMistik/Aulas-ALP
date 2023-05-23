"""Elabore um algoritmo para determinar 
quantas vogais existem dentro de uma 
determinada frase (que deve ser recebida do 
usuário)."""

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
