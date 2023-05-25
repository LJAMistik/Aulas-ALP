"""Faça um algoritmo que receba uma hora
formada por hora e minutos (um número
real), calcule e mostre a hora digitada
apenas em minutos. Lembre-se de que:
Para quatro e meia deve-se digitar: 4,30
Os minutos vão de 0 a 60!"""

hora = float(input("Digite a hora no formato HH.MM: "))

horas_inteiras = int(hora)
minutos_decimal = hora - horas_inteiras

# Converter as horas em minutos
horas_em_minutos = horas_inteiras * 60

# Calcular os minutos totais
minutos_totais = horas_em_minutos + minutos_decimal * 100

print(f"A hora digitada em minutos é: {minutos_totais} minutos")
