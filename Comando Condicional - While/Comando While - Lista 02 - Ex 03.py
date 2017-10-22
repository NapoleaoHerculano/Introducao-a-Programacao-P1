#3. Escreva um programa que receba como entrada 50 números e exiba
#a soma dos que são múltiplos de 3.

cont = 0
soma = 0

while(cont < 5):
    numero=int(input("Digite um valor:"))
    cont += 1

    if numero % 3 == 0:
        soma += numero

print("Soma dos múltiplos de 3:", soma)
