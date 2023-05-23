"""Crie uma função que receba como parâmetro 
3 números interios (representando horas, 
minutos e segundos). A função deve 
converter em segundos.
Por exemplo: 2 h, 40 min e 10 segundos 
correspondem a 9.610 segundos."""

def converter_para_segundos(horas, minutos, segundos):
    total_segundos = (horas * 3600) + (minutos * 60) + segundos
    return total_segundos

# Exemplo de uso da função:
entrada = input("Digite o tempo no formato (hh:mm:ss): ")
horas, minutos, segundos = map(int, entrada.split(":")) # splitpara dividir a entrada em três partes separadas pelos dois pontos
# maps vai converter as partes.

resultado = converter_para_segundos(horas, minutos, segundos)

print(f"{horas:02d}:{minutos:02d}:{segundos:02d} correspondem a {resultado} segundos.")


