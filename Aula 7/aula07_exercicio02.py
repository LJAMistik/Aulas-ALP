"""Faça um algoritmo que calcule a soma dos primeiros 50 
números pares. Este algoritmo não recebe valores do 
teclado. 
Os primeiros números pares são 2, 4, 6..."""

soma = 0
contador = 0
numero = 2

while contador < 50:
    soma += numero
    numero += 2
    contador += 1

print("A soma dos primeiros 50 números pares é:", soma)
