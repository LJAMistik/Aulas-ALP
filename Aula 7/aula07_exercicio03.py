"""Faça um algoritmo que leia o valor do peso e da 
altura de 20 pessoas. Ao final, o algoritmo deve 
mostrar:
- O peso médio
- A altura média
- O maior e o menor IMC
Obs: IMC (Índice de Massa Corporal) – calculado a 
partir da fórmula:
IMC = massa dividido por altura ao quadrado"""

num_pessoas = 20

peso_total = 0
altura_total = 0
imc_maximo = float('-inf')
imc_minimo = float('inf')

for i in range(num_pessoas):
    print(f"\nDados da pessoa {i+1}:")
    peso = float(input("Digite o peso (em kg): "))
    altura = float(input("Digite a altura (em metros): "))

    peso_total += peso
    altura_total += altura

    imc = peso / (altura ** 2)
    if imc > imc_maximo:
        imc_maximo = imc
    if imc < imc_minimo:
        imc_minimo = imc

peso_medio = peso_total / num_pessoas
altura_media = altura_total / num_pessoas

print("\nResultados:")
print("Peso médio:", peso_medio)
print("Altura média:", altura_media)
print("Maior IMC:", imc_maximo)
print("Menor IMC:", imc_minimo)
