"""Faça uma função que determine se um ano 
qualquer, no formato AAAA, é bissexto.
A função retorna 1 se o ano é bissexto e 
0(zero) se não"""

def verificar_ano_bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True  # Ano divisível por 400, é bissexto
            else:
                return False  # Ano divisível por 100, mas não por 400, não é bissexto
        else:
            return 1  # Ano divisível por 4, não é divisível por 100, é bissexto
    else:
        return 0  # Ano não divisível por 4, não é bissexto

# Exemplo de uso da função:
ano = int(input("Digite um ano no formato AAAA: "))
resultado = verificar_ano_bissexto(ano)

if resultado:
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")

