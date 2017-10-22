#2. Escreva um programa que receba como entrada 25 números e exiba a
#quantidade de números que são pares e positivos. 
 
cont = 0
num_pares_positivos = 0


while(cont < 25):
    numero = int(input("Insira um valor:"))
    cont += 1

    if numero %2 == 0 and numero >0:
        num_pares_positivos += 1
    
print("Números Pares e Positivos:", num_pares_positivos)

