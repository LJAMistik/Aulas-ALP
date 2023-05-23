"""Faça um algoritmo que receba o ano de
nascimento de uma pessoa e o ano atual
e mostre:
a) A idade dessa pessoa em anos;
b) A idade dessa pessoa em meses;
c) A idade dessa pessoa em dias;
d) A idade dessa pessoa em semanas.
"""
# OBSERVAÇÃO: IGNOREI O ANO BISSEXTO

# Pedir o ano de nascimento:
ano_nasc = int(input("Digite seu ano de nascimento, com os quatros dígitos: "))

# Pedir o ano atual:
ano_atual = int(input("Digite o ano atual, com os quatro dígitos: "))

# Calcular e mostrar os anos:
anos = ano_atual - ano_nasc
print(f"Você possui a idade de {anos} anos.")

# Calcular e mostrar os meses, precisa multiplicar por quantos meses tem o ano:
ano_atual_conv =  ano_atual * 12
ano_nasc_conv = ano_nasc * 12
meses = ano_atual_conv - ano_nasc_conv
print(f"Ou {meses} meses.")

# Calcular e mostrar em dias, precisa multiplicar por quantos dias tem o ano:
ano_atual_conv_dias =  ano_atual * 365
ano_nasc_conv_dias = ano_nasc * 365
dias = ano_atual_conv_dias - ano_nasc_conv_dias
print(f"Totalizando {dias} dias.")

# Calcular e mostrar as semanas, precisa dividir dias por semanas, usando a divisão inteira:
ano_atual_conv_semanas = ano_atual_conv_dias // 7
ano_nasc_conv_semanas = ano_nasc_conv_dias // 7
semanas = ano_atual_conv_semanas - ano_nasc_conv_semanas
print(f"Que é o mesmo que {semanas} semanas.")