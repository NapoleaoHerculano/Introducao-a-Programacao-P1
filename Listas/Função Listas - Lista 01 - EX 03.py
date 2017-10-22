#3. Escreva um programa que crie uma lista com 8 números inteiros informados pelo usuário e
#exiba apenas aqueles que são múltiplos de 3.

multiplos3 = []


for i in range(8):
    num=int(input("Nº:"))
    if num % 3 == 0:
        multiplos3.append(num)

print("Multiplos de 3:", multiplos3)
