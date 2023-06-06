# Definir uma lista vazia para armazenar os dados das pessoas
pessoas = []

# Loop para inserir os dados das pessoas
while True:
    sobrenome = input("Digite o sobrenome da pessoa (ou pressione <Enter> para sair): ")
    if not sobrenome:
        break

    idade = input("Digite a idade da pessoa: ")
    while not idade.isdigit():  # Verificar se a idade é um número válido
        print("Idade inválida. Digite novamente.")
        idade = input("Digite a idade da pessoa: ")

    altura = input("Digite a altura da pessoa em centímetros: ")
    while not altura.isdigit():  # Verificar se a altura é um número válido
        print("Altura inválida. Digite novamente.")
        altura = input("Digite a altura da pessoa em centímetros: ")

    peso = input("Digite o peso da pessoa em kg: ")
    while not peso.isdigit():  # Verificar se o peso é um número válido
        print("Peso inválido. Digite novamente.")
        peso = input("Digite o peso da pessoa em kg: ")

    # Adicionar os dados da pessoa à lista de pessoas
    pessoas.append({"sobrenome": sobrenome, "idade": int(idade), "altura": int(altura), "peso": int(peso)})

# Ordenar a lista de pessoas em ordem alfabética pelo sobrenome
pessoas.sort(key=lambda x: x["sobrenome"])

# Mostrar a listagem das pessoas
print("Listagem das pessoas:")
for pessoa in pessoas:
    print("Sobrenome:", pessoa["sobrenome"])
    print("Idade:", pessoa["idade"])
    print("Altura:", pessoa["altura"], "cm")
    print("Peso:", pessoa["peso"], "kg")
    print()

# Calcular a média da idade, altura e peso
total_pessoas = len(pessoas)
soma_idades = sum([pessoa["idade"] for pessoa in pessoas])
media_idade = soma_idades / total_pessoas

soma_alturas = sum([pessoa["altura"] for pessoa in pessoas])
media_altura = soma_alturas / total_pessoas

soma_pesos = sum([pessoa["peso"] for pessoa in pessoas])
media_peso = soma_pesos / total_pessoas

# Mostrar o resumo da tabela com as médias
print("Resumo:")
print("Média de idade:", media_idade)
print("Média de altura:", media_altura, "cm")
print("Média de peso:", media_peso, "kg")
