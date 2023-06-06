"""Faça um programa que carregue uma lista com
os modelos de cinco carros (exemplos de modelos: Onix,
Polo, Kicks etc.). Carregue uma outra lista com o
consumo desses carros, isto é, quantos quilômetros cada
um desses carros faz com um litro de combustivel.
Calcule e mostre:
a) O modelo do carro mais econômico;
b) Quantos litros de combustível cada um dos carros
cadastrados consome pra percorrer para percorrer uma
distância de 1000 quilometros e quanto isto custará,
considerando um que a gasolina custe R$ 5,65 o litro.
Abaixo segue uma tela de exemplo. O disposição das
informação deve ser o mais próxima possível ao exemplo.
Os dados são ficticios e podem mudar a cada execução do
programa.
Comparativo de Consumo de Combustivel
Veiculo 1
Nome: onix
km por litro: 7
Veiculo 2
Nome: polo
km por litro: 10
Veiculo 3
Nome: cronos
km por litro: 12.5
Veiculo 4
Nome: kicks
km por litro: 9
Veiculo 5
Nome: kwid
km por litro: 14.5

Relatorio Final
1 - onix    -   7.0     142.9 litros R$ 807.38
2 - polo    -   10.0    100.0 litros R$ 565.00
3 - cronos  -   12.5    080.0 litros R$ 452.00
4 - kicks   -   9.0     111.1 litros R$ 627.71
5 - kwid    -   14.5    069.0 litros R$ 389.95
o menor consumo é do kwid
"""
def calcular_consumo(distancia, consumo, preco_gasolina):
    litros = distancia / consumo
    custo = litros * preco_gasolina
    return litros, custo


try:
    modelos = []
    consumos = []

    for i in range(5):
        modelo = input("Informe o modelo do carro {}: ".format(i + 1))
        consumo = float(input("Informe o consumo do carro {} (km/l): ".format(i + 1)))

        modelos.append(modelo)
        consumos.append(consumo)

    # Encontrar o carro mais econômico
    indice_menor_consumo = consumos.index(min(consumos))
    carro_mais_economico = modelos[indice_menor_consumo]

    print("\nComparativo de Consumo de Combustível")
    for i in range(len(modelos)):
        litros, custo = calcular_consumo(1000, consumos[i], 5.65)
        print("{} - {} - {:.1f} - {:.1f} litros - R$ {:.2f}".format(i + 1, modelos[i], consumos[i], litros, custo))

    print("\nO menor consumo é do {}".format(carro_mais_economico))

except ValueError:
    print("Valor inválido. Certifique-se de informar corretamente o consumo do carro.")



